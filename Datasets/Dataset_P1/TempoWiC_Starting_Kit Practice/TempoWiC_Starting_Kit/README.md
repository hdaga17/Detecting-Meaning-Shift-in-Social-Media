# TempoWiC Shared Task

This folder contains the starting kit for the TempoWiC Shared Task for EvoNLP: The First Workshop on Ever Evolving NLP, co-located with EMNLP 2022.

For more details about the task, please visit:
https://sites.google.com/view/evonlp/shared-task


Below you may find some details about each file contained in this folder.


## DATA - INSTANCES (data/*.jl)

Contains instances with pairs of tweets and respective dates. It's organized as jsonlines (one instance per line), using the following structure for each instance:

```
{
  "id": str,            # instance id
  "word": str,          # target word (lemmatized)
  "tweet1": {
    "text": str,        # raw text
    "tokens": list,     # tokenized text
    "token_idx": int,   # token index for the target word in the tokenized text
    "text_start": int,  # character index for the first position of target word in the raw text
    "text_end": int,    # character index for the last position of target word in the raw text
    "date": str         # tweet1's date in YYYY-MM format
  },
  "tweet2": {
    "text": str,        # raw text
    "tokens": list,     # tokenized text
    "token_idx": int,   # token index for the target word
    "text_start": int,  # character index for the first position of target word
    "text_end": int,    # character index for the last position of target word
    "date": str         # tweet2's date in YYYY-MM format
  }
}
```

Tweets have been tokenized using NLTK's TweetTokenizer and both the raw and tokenized versions of the tweets are provided.

This starting kit includes the following sets:
- Trial (20 instances, for practicing submissions)
- Training (1,428 instances)
- Validation (396 instances)
- NEW 01/08: Test (10,000 instances, includes dummy instances to discourage cheating)


## DATA - GOLD STANDARD (data/*.labels.tsv)

Contains gold labels for each instance. One id/label per line, following the format "`<instance id><tab><0 if False, 1 if True>`".

Labels for test instances are hidden.


## READING JSON (pprint.py)

Outputs instance data stored as .jl in a more readable format. For easier inspection.

```bash
python data/pprint.py trial.data.jl
```


## RANDOM BASELINE (random_baseline.py)

A script showing how to load the dataset and generate a predictions file compatible with the scorer. Generates `trial.random-preds.tsv`.

```bash
python random_baseline.py 
```


## EVALUATION SCORER (score.py)

A simple python script to generate official scores for the task. Reports accuracy and macro-f1. To be used as follows:

```bash
python score.py predictions/trial.random-preds.tsv data/trial.gold.tsv
```

Predictions need to be stored in a .tsv file where each line corresponds to the tweet id of the instance and 0 (if the meaning of the target word has not changed) or 1 (if the meaning of the target word is different in both tweets). See "predictions/trial.random-preds.tsv" as an example.
