#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from model.py import build_train_test_cnn_model

train_data = pd.read_csv('../csv_files/Model/train.csv')
X_train = train_data.iloc[:-1,:-1]
Y_train = train_data.iloc[:-1,-1]

test_data = pd.read_csv('../csv_files/Model/test.csv')
X_test = test_data.iloc[:-1,:-1]
Y_test = test_data.iloc[:-1,-1]

validate_data = pd.read_csv('../csv_files/Model/validate.csv')
X_val = validate_data.iloc[:-1,:-1]
Y_val = validate_data.iloc[:-1,-1]

epoch = 20
hyperparameters_to_test = [

    # Different Filters
    {'filters': 32, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 16, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 128, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},

    # Different Kernel Sizes
    {'filters': 64, 'kernel_size': 4, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 5, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 6, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 7, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},

    # Different Dense Units
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 256, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 512, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 1024, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},

    # Different Dropout
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.4, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.3, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.2, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.1, 'epochs': epoch, 'batch_size': 32, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},

    # Different Batch Size
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 64, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 128, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 256, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4},
    {'filters': 64, 'kernel_size': 3, 'pool_size': 2, 'dense_units': 128, 'dropout_rate': 0.5, 'epochs': epoch, 'batch_size': 512, 'learning_rate': 0.001, 'use_early_stopping': True, 'patience': 3, 'num_conv_layers': 4}
]


cnn_results = []

for params in hyperparameters_to_test:
    test_acc = build_train_test_cnn_model(X_train, Y_train, X_val, Y_val, X_test, Y_test, **params)
    cnn_results.append((params, test_acc))
    print(f"Parameters: {params}")
    print(f"Test Accuracy: {test_acc:.4f}")
    print("===================")

# Plot
parameters = [str(params) for params, _ in cnn_results]
test_results = [result for _, result in cnn_results]

plt.figure(figsize=(8, 12))

plt.barh(parameters, test_results, color='skyblue', height=0.5)
plt.xlabel('Test Results')
plt.ylabel('Parameters')
plt.title('CNN Model Test Results for Different Parameters, 10 Epochs')
plt.xlim(min(test_results) - 0.01, max(test_results) + 0.01)
plt.tight_layout()

plt.savefig('../Results/cnn_results.png')

# Save
file_path = '../Results/cnn_results.txt'

with open(file_path, 'w') as file:
    file.write("./Parameters,Test Results\n")

    for params, result in cnn_results:
        parameters_str = ', '.join(f"{key}={value}" for key, value in params.items())
        file.write(f"{parameters_str},{result}\n")
