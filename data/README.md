# Data

One folder per task, named as in the book's tables. Each folder has a README with the source paper, the replication archive and its license, how the spreadsheet was built, and the class counts. Every spreadsheet has a `text` column and a human-coded `label_main` column; the notebooks and scripts read those two.

| Folder | Task | N | Classes | Redistributed | License of the archive |
|---|---|---|---|---|---|
| `erhard_popbert` | PopBERT: populism in Bundestag speeches | 8,795 | 2 | full | CC0 1.0 |
| `parlacap` | ParlaCAP: policy topics of parliamentary speeches | 3,443 | 22 | not included | available from the authors |
| `heseltine` | Negativity in politicians' tweets and news text | 2,195 | 2 | full | CC0 1.0 |
| `proksch` | Sentiment of 2010 State of the European Union debate paragraphs | 301 | 9 values, collapsed to 5 | full | CC0 1.0 |
| `fowler_ads` | Tone of 2018 television and Facebook political ads | 14,445 | 3 | labels only | custom terms, no redistribution |
| `vanderveen_populism` | Populist, pluralist and neutral sentences in governor and presidential speeches | 3,624 | 3 | full | CC0 1.0 |
| `ballard_incivility` | Incivility in tweets by members of Congress | 2,919 | 2 | full | CC0 1.0 |
| `foy_sutherland` | Tone of campaign "redbox" messages | 910 | 3 | full | CC0 1.0 |
| `kostovicova_paskhalis` | Deliberative quality of speech acts in transitional-justice consultations | 1,211 | 4 | full | CC0 1.0 |
| `dietrich` | Aid mentions in party manifesto sentences | 52,744 | 2 | full | CC0 1.0 |
| `goes_chapman` | Governance advice in IMF Article IV staff appraisals | 700 | 2 | full | CC0 1.0 |
| `trubowitz_watanabe` | Geopolitical threat in New York Times foreign-affairs articles | 1,700 | 3 | full | CC0 1.0 |

Eleven archives are on Harvard Dataverse. Ten are released under CC0 1.0, and their texts are included as used in the book. The Fowler et al. archive restricts distribution to Dataverse, so `fowler_ads/` holds the labels and identifiers with code that rebuilds the texts from the archive. ParlaCAP is not included; its folder explains how to obtain the data.

Four folders also carry the row-level files behind Chapter 5: decoder predictions per row, covariates, and the encoder's out-of-fold predictions.
