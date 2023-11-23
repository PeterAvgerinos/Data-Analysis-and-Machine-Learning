#!/usr/bin/env python3

import pandas as pd
import numpy as np
from glob import glob
from sklearn.model_selection import train_test_split

def add_noise(df, noise_level=0.1):
    data_range = df.max() - df.min()

    noise = np.random.normal(scale=noise_level*data_range, size=df.shape)
    return df + noise

paths = glob('../csv_files/MLII/MLII_*.csv')
dfs = []

for path in paths:
    df = pd.read_csv(path)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)

features = combined_df.iloc[:, :-1]
labels = combined_df.iloc[:, -1]

augmented_features = []
augmented_labels = []

for index, row in features.iterrows():
    noisy_feature = add_noise(row)
    augmented_features.append(noisy_feature.values)
    augmented_labels.append(labels[index])

augmented_features = pd.DataFrame(augmented_features, columns=features.columns)
augmented_labels = pd.Series(augmented_labels, name=labels.name)

augmented_data = pd.concat([augmented_features, augmented_labels], axis=1)

combined_df = pd.concat([augmented_data, combined_df], ignore_index=True)
combined_df = combined_df.sample(frac=1).reset_index(drop=True)

train_val, test = train_test_split(combined_df, test_size=0.15, random_state=42)
train, validate = train_test_split(train_val, test_size=0.15, random_state=42)

train.to_csv('../csv_files/Model/train.csv', index=False)
validate.to_csv('../csv_files/Model/validate.csv', index=False)
test.to_csv('../csv_files/Model/test.csv', index=False)
