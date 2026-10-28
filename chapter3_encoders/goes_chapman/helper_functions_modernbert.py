#####
## HELPER FUNTIONS FOR BASIC CLASSIFIER
## Created by: Joan C. Timoneda 
## Date: Jun 11 2021
#####

import seaborn as sns
import matplotlib.pyplot as plt
import datetime 
import time
import numpy as np

def good_update_interval(total_iters, num_desired_updates):
    exact_interval = total_iters / num_desired_updates
    order_of_mag = len(str(total_iters)) - 1
    round_mag = order_of_mag - 1
    update_interval = int(round(exact_interval, -round_mag))
    if update_interval == 0:
        update_interval = 1
    return update_interval
    
def format_time(elapsed):
    elapsed_rounded = int(round((elapsed)))
    return str(datetime.timedelta(seconds=elapsed_rounded)) 

def plot_distribution(list_lengths):
    sns.set(style='darkgrid')
    sns.set(font_scale=1.5)
    plt.rcParams["figure.figsize"] = (10,5)
    trunc_lengths = [min(l, 512) for l in list_lengths]
    sns.distplot(trunc_lengths, kde=False, rug=False)
    plt.title('Comment Lengths')
    plt.xlabel('Comment Length')
    plt.ylabel('# of Comments')

def plot_distribution_modernbert(list_lengths, max_len=1024, roberta_cutoff=512):
    """Token-length distribution for long-context models: no clipping, full
    range to max_len, with the RoBERTa cutoff and the chosen max_len marked."""
    sns.set(style='darkgrid')
    sns.set(font_scale=1.5)
    plt.rcParams["figure.figsize"] = (10, 5)
    upper = max(max_len, max(list_lengths))
    sns.histplot(list_lengths, bins=np.arange(0, upper + 16, 16))
    plt.axvline(roberta_cutoff, color='red', linestyle='--', linewidth=1.5,
                label=f'RoBERTa cutoff ({roberta_cutoff})')
    plt.axvline(max_len, color='blue', linestyle='--', linewidth=1.5,
                label=f'max_len ({max_len})')
    plt.xlim(0, upper)
    plt.title('Comment Lengths')
    plt.xlabel('Comment Length (tokens)')
    plt.ylabel('# of Comments')
    plt.legend()
    plt.show()
    
def plot_loss(df):
    sns.set(style='darkgrid')
    sns.set(font_scale=1.5)
    plt.rcParams["figure.figsize"] = (12,6)
    plt.plot(df['Training Loss'], 'b-o', label="Training")
    plt.plot(df['Valid. Loss'], 'g-o', label="Validation")
    plt.title("Training & Validation loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.xticks(list(range(1, epochs+1)))
    plt.show()


def plot_loss_cv(df, epochs):
    sns.set(style='darkgrid')
    sns.set(font_scale=1.5)
    plt.rcParams["figure.figsize"] = (12,6)
    plt.plot(df.iloc[0,:], 'b-o', label="Training")
    plt.plot(df.iloc[1,:], 'g-o', label="Validation")
    plt.title("Training & Validation loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.xticks(list(range(1, epochs+1)))
    plt.show()



 
    
    
    