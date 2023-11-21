#!/usr/bin/env python3

import pandas as pd
from glob import glob
from sklearn.model_selection import train_test_split

paths = glob('../csv_files/MLII/MLII_*.csv')
dfs = []

for path in paths:
    df = pd.read_csv(path)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

train_val, test = train_test_split(combined_df, test_size=0.15, random_state=42)
train, validate = train_test_split(train_val, test_size=0.15, random_state=42)

train.to_csv('../csv_files/Model/train.csv', index=False)
validate.to_csv('../csv_files/Model/validate.csv', index=False)
test.to_csv('../csv_files/Model/test.csv', index=False)
