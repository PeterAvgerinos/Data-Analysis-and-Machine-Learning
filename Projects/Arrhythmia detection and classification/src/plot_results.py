import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

data = pd.read_csv('../Final/cnn_results.csv')
results = data.iloc[:,1:]

for column in results.columns:
    plt.figure(figsize=(14, 12))

    plt.barh(data['Parameters'], data[f"{column}"], color='skyblue', height=0.5)
    plt.xlabel('Test Results')
    plt.ylabel('Parameters')
    plt.title(f'CNN Model {column} Results, Average: {data[column].mean()}')
    plt.xlim(min(data[f"{column}"]) - 0.01, max(data[f"{column}"]) + 0.01)

    plt.savefig(f'../Final/{column}.png')


