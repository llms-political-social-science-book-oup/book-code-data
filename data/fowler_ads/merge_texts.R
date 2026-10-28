# Rebuild the ad texts used in the book from the authors' replication archive
# (Harvard Dataverse doi:10.7910/DVN/IR9XGC, file ads_online_offline_replication.tar.gz).
#
# Usage:  Rscript merge_texts.R /path/to/ads_online_offline_replication/data
# Output: fowler_ads_rebuilt_text.csv next to this script (page_id, snapshot_id, text).
# Then run: python merge_texts.py
#
# The text of an ad is the concatenation, separated by one space, of the distinct
# non-missing text features the archive stores for it (Facebook creative body,
# image text, video transcript, video frame text), grouped by page_id and
# snapshot_id. This follows the archive's own read_ad_features.R, with repeated
# segments kept once.
suppressMessages({library(dplyr)})
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) stop("give the path to the archive's data/ folder")
d <- args[1]
load(file.path(d, "ad_features", "all_features_fb.RData"))
load(file.path(d, "ad_features", "all_features_tv.RData"))
texts <- bind_rows(fb_features, tv_features) %>%
  group_by(page_id, snapshot_id) %>%
  summarize(text = paste(unique(text[!is.na(text)]), collapse = " "), .groups = "drop")
out <- file.path(dirname(normalizePath(sub("--file=", "", grep("--file=", commandArgs(), value = TRUE)))), "fowler_ads_rebuilt_text.csv")
write.csv(texts, out, row.names = FALSE)
cat("wrote", out, "with", nrow(texts), "ads\n")
