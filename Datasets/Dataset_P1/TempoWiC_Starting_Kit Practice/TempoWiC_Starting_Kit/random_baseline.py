"""
A script showing how to load the dataset and generate a predictions file compatible with the scorer. Generates 'predictions/trial.random-preds.tsv'.
"""

import json
import random


def load_instances(fn):

    instances = []
    with open(fn) as f:
        for jl_str in f:
            instances.append(json.loads(jl_str))
    
    return instances


if __name__ == '__main__':

    trial_instances = load_instances('data/trial.data.jl')


    # generate predictions
    trial_predictions = {}
    for inst in trial_instances:
        pred = random.choice([0, 1])
        trial_predictions[inst['id']] = pred


    # output predictions
    with open('predictions/trial.random-preds.tsv', 'w') as preds_f:
        for inst_id, pred in trial_predictions.items():
            preds_f.write(f"{inst_id}\t{pred}\n")
