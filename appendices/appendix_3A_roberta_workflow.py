"""
Appendix 3.A -- A complete encoder fine-tuning workflow (Chapter 3).

Fine-tunes RoBERTa-large on the van der Veen (2024) populism sentences with
ten-times repeated 10-fold cross-validation, saves the out-of-fold predictions
for Chapter 5, fine-tunes a final model on all the data, and labels new text.
The blocks below are the listings printed in the appendix, in order.

Data: a spreadsheet with a "text" column and a human-coded "label_main" column
(vanderveen_populism_text_labels.xlsx, in data/vanderveen_populism/).
Requirements: pip install torch transformers pandas numpy scikit-learn openpyxl
helper_functions.py must sit next to this script. A GPU is needed.
"""


# ========================================================================
# Block 1. Libraries
# ========================================================================
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from transformers import get_linear_schedule_with_warmup
from torch.optim import AdamW
import torch
from torch.utils.data import TensorDataset, DataLoader, Subset
from torch.utils.data import SubsetRandomSampler
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
import time
import random
import helper_functions as hf   # progress/plot helpers, in the repository


# ========================================================================
# Block 2. Data
# ========================================================================
data = pd.read_excel("vanderveen_populism_text_labels.xlsx")
data = data.dropna(subset=["text"]).reset_index(drop=True)
data = data.sample(frac=1, random_state=6).reset_index(drop=True)
print(data["label_main"].value_counts())

data["label"] = data["label_main"].astype("category")
label_names = list(data["label"].cat.categories)   # alphabetical order
num_labels = len(label_names)
data["label"] = data["label"].cat.codes            # 0, 1, 2
print(data.head())


# ========================================================================
# Block 3. Tokenization and sequence length
# ========================================================================
tokenizer = RobertaTokenizer.from_pretrained("roberta-large")

lengths = []
for x, row in data.iterrows():
    encoded_sent = tokenizer.encode(row["text"], add_special_tokens=True)
    lengths.append(len(encoded_sent))

print("{:>10,} texts".format(len(lengths)))
print("   Min length: {:,} tokens".format(min(lengths)))
print("   Max length: {:,} tokens".format(max(lengths)))
print("Median length: {:,} tokens".format(int(np.median(lengths))))
hf.plot_distribution(lengths)

max_len = 100   # chosen after looking at the distribution; 512 is the ceiling
num_truncated = np.sum(np.greater(lengths, max_len))
print("{:,} of {:,} texts ({:.1%}) are longer than {} tokens.".format(
    num_truncated, len(lengths), num_truncated / len(lengths), max_len))

input_ids = []
attn_masks = []
labels = []
for x, row in data.iterrows():
    encoded_dict = tokenizer(row["text"], max_length=max_len,
                             padding="max_length", truncation=True,
                             return_tensors="pt")
    input_ids.append(encoded_dict["input_ids"])
    attn_masks.append(encoded_dict["attention_mask"])
    labels.append(row["label"])

input_ids = torch.cat(input_ids, dim=0)
attn_masks = torch.cat(attn_masks, dim=0)
labels = torch.tensor(labels)
dataset = TensorDataset(input_ids, attn_masks, labels)


# ========================================================================
# Block 4. Hyperparameters
# ========================================================================
model_name = "roberta-large"
lr = 3e-5            # Section 3.5 starting point; can go down to 1e-5
epochs = 4           # fixed; no early stopping in the scarce-data scenario
batch_size = 32      # 16 if the texts are long and the GPU runs out of memory
warmup_frac = 0.06   # 6% of the optimizer steps as linear warmup
k_folds = 10
n_runs = 10          # 10 x 10 = 100 models, the protocol used in the book

# Degenerate-run protection. If training F1 at these epochs is below the
# threshold, the model has collapsed to one class: restart the fold with
# a fresh initialization, report it, and keep it out of the average.
collapse_checkpoints = {2: 0.40, 3: 0.55}   # epoch (1-indexed): minimum F1
max_retries = 3


# ========================================================================
# Block 5. Seeds and device
# ========================================================================
seed_val = 6
random.seed(seed_val)
np.random.seed(seed_val)
torch.manual_seed(seed_val)
torch.cuda.manual_seed_all(seed_val)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.cuda.empty_cache()


# ========================================================================
# Block 6. Ten-times repeated 10-fold cross-validation
# ========================================================================
all_runs_stats = []
oof = data[["text", "label_main"]].copy()   # out-of-fold predictions
collapses = 0
total_t0 = time.time()

for run in range(n_runs):

    fold_stats = []
    kfold = KFold(n_splits=k_folds, shuffle=True, random_state=seed_val + run)

    for fold, (train_ids, test_ids) in enumerate(kfold.split(dataset)):
        print("RUN {}  FOLD {}".format(run + 1, fold + 1))
        print("--------------------------------")

        train_sampler = SubsetRandomSampler(train_ids)
        train_dataloader = DataLoader(dataset, batch_size=batch_size,
                                      sampler=train_sampler)
        test_dataloader = DataLoader(Subset(dataset, test_ids),
                                     batch_size=batch_size)   # keeps row order

        # ============= TRAIN (with collapse detection and retry) =============
        for attempt in range(max_retries + 1):

            if attempt > 0:
                print("  >> Restarting fold with a fresh initialization "
                      "(attempt {} of {})".format(attempt + 1, max_retries + 1))
                collapses += 1

            model = RobertaForSequenceClassification.from_pretrained(
                model_name, num_labels=num_labels)
            model.to(device)
            optimizer = AdamW(model.parameters(), lr=lr, eps=1e-6)
            total_steps = len(train_dataloader) * epochs
            scheduler = get_linear_schedule_with_warmup(
                optimizer, num_warmup_steps=int(warmup_frac * total_steps),
                num_training_steps=total_steps)
            collapsed = False

            for epoch_i in range(epochs):
                print("")
                print("======== Epoch {} / {} ========".format(epoch_i + 1,
                                                              epochs))
                t0 = time.time()
                total_train_loss = 0
                model.train()
                update_interval = hf.good_update_interval(
                    total_iters=len(train_dataloader), num_desired_updates=10)
                predictions_t, true_labels_t = [], []

                for step, batch in enumerate(train_dataloader):
                    if (step % update_interval) == 0 and step != 0:
                        elapsed = hf.format_time(time.time() - t0)
                        print("  Batch {:>5,} of {:>5,}.  Elapsed: {}.".format(
                            step, len(train_dataloader), elapsed), end="\r")

                    b_input_ids = batch[0].to(device)
                    b_input_mask = batch[1].to(device)
                    b_labels = batch[2].to(device)

                    model.zero_grad()
                    outputs = model(b_input_ids, attention_mask=b_input_mask,
                                    labels=b_labels)
                    loss = outputs.loss
                    logits = outputs.logits

                    total_train_loss += loss.item()
                    loss.backward()
                    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                    optimizer.step()
                    scheduler.step()

                    predictions_t.append(logits.detach().cpu().numpy())
                    true_labels_t.append(b_labels.cpu().numpy())

                flat_predictions_t = np.concatenate(predictions_t, axis=0)
                flat_true_labels_t = np.concatenate(true_labels_t, axis=0)
                predicted_labels_t = np.argmax(flat_predictions_t, axis=1)
                f1_t = f1_score(flat_true_labels_t, predicted_labels_t,
                                average="macro")
                avg_train_loss = total_train_loss / len(train_dataloader)

                print("")
                print("  Average training loss: {:.3f}".format(avg_train_loss))
                print("  Training F1: {:.3f}".format(f1_t))
                print("  Training epoch took: {}".format(
                    hf.format_time(time.time() - t0)))

                # collapse detection
                threshold = collapse_checkpoints.get(epoch_i + 1)
                if (threshold is not None and f1_t < threshold
                        and attempt < max_retries):
                    print("  !! Collapse detected: training F1 {:.3f} < {} "
                          "at epoch {}".format(f1_t, threshold, epoch_i + 1))
                    collapsed = True
                    break

            if not collapsed:
                break   # training succeeded, leave the retry loop

            del model, optimizer, scheduler   # clean up before retrying
            torch.cuda.empty_cache()

        # ============= TEST =============
        model.eval()
        predictions, true_labels = [], []
        for batch in test_dataloader:
            b_input_ids = batch[0].to(device)
            b_input_mask = batch[1].to(device)
            b_labels = batch[2].to(device)
            with torch.no_grad():
                outputs = model(b_input_ids, attention_mask=b_input_mask)
            predictions.append(outputs.logits.detach().cpu().numpy())
            true_labels.append(b_labels.cpu().numpy())

        flat_predictions = np.concatenate(predictions, axis=0)
        predicted_labels = np.argmax(flat_predictions, axis=1)
        true_labels = np.concatenate(true_labels, axis=0)

        all_labels = list(range(num_labels))
        macro_f1 = f1_score(true_labels, predicted_labels, average="macro",
                            labels=all_labels, zero_division=0)
        class_f1 = f1_score(true_labels, predicted_labels, average=None,
                            labels=all_labels, zero_division=0)

        for i, name in enumerate(label_names):
            print("  {} F1: {:.3f}".format(name, class_f1[i]))
        print("  Macro F1: {:.3f}".format(macro_f1))
        if len(np.unique(predicted_labels)) == 1:
            print("  !! Degenerate fold: one label for every text. Report it.")

        stats = {"run": run + 1, "fold": fold + 1,
                 "train_loss": avg_train_loss, "macro_f1": macro_f1}
        for i, name in enumerate(label_names):
            stats["f1_" + name] = class_f1[i]
        fold_stats.append(stats)

        predicted_names = [label_names[p] for p in predicted_labels]
        oof.loc[test_ids, "pred_run" + str(run + 1)] = predicted_names

        del model, optimizer, scheduler   # free the GPU for the next fold
        torch.cuda.empty_cache()

    # ============= PER-RUN SUMMARY =============
    run_df = pd.DataFrame(fold_stats)
    print("")
    print("RUN {} over {} folds: macro F1 mean {:.3f}, SD {:.3f}".format(
        run + 1, k_folds, run_df["macro_f1"].mean(), run_df["macro_f1"].std()))
    for name in label_names:
        print("  {} F1 mean: {:.3f}".format(name, run_df["f1_" + name].mean()))
    all_runs_stats.append(run_df)
    
    with open("vanderveen_results_run{}.txt".format(run + 1), "w") as outfile:
        outfile.write(run_df.to_string(index=False))
        
print("Total training time: {}".format(hf.format_time(time.time() - total_t0)))


# ========================================================================
# Block 7. Summary and saved results
# ========================================================================
results = pd.concat(all_runs_stats, ignore_index=True)
results.to_csv("vanderveen_roberta_cv_results.csv", index=False)
oof.to_csv("vanderveen_roberta_oof_predictions.csv", index=False)

run_means = results.groupby("run")["macro_f1"].mean()
print("")
print("========== FINAL SUMMARY ({} runs x {} folds) ==========".format(
    n_runs, k_folds))
print("Macro F1: mean {:.3f}, SD across runs {:.3f}".format(
    run_means.mean(), run_means.std()))
for name in label_names:
    print("  {} F1: {:.3f}".format(name, results["f1_" + name].mean()))
print("Collapsed attempts restarted: {}".format(collapses))


# ========================================================================
# Block 8. The final model
# ========================================================================
all_ids = range(len(dataset))
train_dataloader = DataLoader(dataset, batch_size=batch_size,
                              sampler=SubsetRandomSampler(all_ids))
model = RobertaForSequenceClassification.from_pretrained(
    model_name, num_labels=num_labels)
model.to(device)
optimizer = AdamW(model.parameters(), lr=lr, eps=1e-6)
total_steps = len(train_dataloader) * epochs
scheduler = get_linear_schedule_with_warmup(
    optimizer, num_warmup_steps=int(warmup_frac * total_steps),
    num_training_steps=total_steps)

model.train()
for epoch_i in range(epochs):
    for step, batch in enumerate(train_dataloader):
        b_input_ids = batch[0].to(device)
        b_input_mask = batch[1].to(device)
        b_labels = batch[2].to(device)
        model.zero_grad()
        outputs = model(b_input_ids, attention_mask=b_input_mask,
                        labels=b_labels)
        outputs.loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()
    print("Epoch {} / {} done".format(epoch_i + 1, epochs))

model.config.id2label = dict(enumerate(label_names))
model.config.label2id = dict(zip(label_names, range(num_labels)))
model.save_pretrained("roberta_populism_final")
tokenizer.save_pretrained("roberta_populism_final")


# ========================================================================
# Block 9. Labeling new text
# ========================================================================
# Load the saved model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained("roberta_populism_final")
model = RobertaForSequenceClassification.from_pretrained("roberta_populism_final")
model.to(device)
model.eval()

# New, unlabeled texts (or a column from a new spreadsheet)
new_data = pd.DataFrame({"text": [
    "The people have spoken and a new direction has been decided.",
    "Our reserves are up, our exports are up, our state GDP is up.",
    "We must bring Democrats and Republicans together on this."]})
# new_data = pd.read_excel("new_speeches.xlsx")

# Tokenize exactly as in Block 3, with the same max_len
input_ids = []
attn_masks = []
for x, row in new_data.iterrows():
    encoded_dict = tokenizer(row["text"], max_length=max_len,
                             padding="max_length", truncation=True,
                             return_tensors="pt")
    input_ids.append(encoded_dict["input_ids"])
    attn_masks.append(encoded_dict["attention_mask"])
input_ids = torch.cat(input_ids, dim=0)
attn_masks = torch.cat(attn_masks, dim=0)
new_dataset = TensorDataset(input_ids, attn_masks)
new_dataloader = DataLoader(new_dataset, batch_size=batch_size)  # keeps row order

# Predict, batch by batch, without updating any weights
predictions = []
for batch in new_dataloader:
    b_input_ids = batch[0].to(device)
    b_input_mask = batch[1].to(device)
    with torch.no_grad():
        outputs = model(b_input_ids, attention_mask=b_input_mask)
    predictions.append(outputs.logits.detach().cpu().numpy())

flat_predictions = np.concatenate(predictions, axis=0)
predicted_codes = np.argmax(flat_predictions, axis=1)
probabilities = torch.softmax(torch.tensor(flat_predictions), dim=1).numpy()

# Codes back to label names, and save next to the text
predicted_names = []
for code in predicted_codes:
    predicted_names.append(label_names[code])
new_data["label_pred"] = predicted_names
new_data["prob_pred"] = probabilities.max(axis=1)
print(new_data)
new_data.to_excel("new_speeches_labeled.xlsx", index=False)
