#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from model.py import build_train_test_rnn_model

train_data = pd.read_csv('../csv_files/Model/train.csv')
X_train = train_data.iloc[:-1,:-1]
Y_train = train_data.iloc[:-1,-1]

test_data = pd.read_csv('../csv_files/Model/test.csv')
X_test = test_data.iloc[:-1,:-1]
Y_test = test_data.iloc[:-1,-1]

validate_data = pd.read_csv('../csv_files/Model/validate.csv')
X_val = validate_data.iloc[:-1,:-1]
Y_val = validate_data.iloc[:-1,-1]

# List of hyperparameters to test
hyperparameters_to_test = [

]

rnn_results = []

# Build Train Test
for params in hyperparameters_to_test:
    val_acc, test_acc = build_train_test_rnn_model(X_train, Y_train, X_val, Y_val, X_test, Y_test, **params)
    rnn_results.append((params, test_acc))
    print(f"Parameters: {params}")
    print(f"Validation Accuracy: {val_acc:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")
    print("===================")

# Plot
parameters = [str(params) for params, _ in rnn_results]
test_results = [result for _, result in rnn_results]

plt.figure(figsize=(12, 6))
plt.bar(parameters, test_results, color='skyblue', width = 0.5)
plt.xlabel('Parameters')
plt.ylabel('Test Results')
plt.title('CNN Model Test Results for Different Parameters, 10 Epochs')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('../Results/rnn_results.png')

# Save
file_path = '../Results/rnn_results.txt'

with open(file_path, 'w') as file:
    file.write("./Parameters,Test Results\n")  # Header

    for params, result in rnn_results:
        parameters_str = ', '.join(f"{key}={value}" for key, value in params.items())
        file.write(f"{parameters_str},{result}\n")
