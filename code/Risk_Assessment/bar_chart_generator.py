import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('filtered_data.csv')

acc = df.sum()

plt.figure(figsize=(23, 7))  

plt.bar(acc.index, acc.values)


plt.xlabel('Classes')
plt.ylabel('Number of people')
plt.title('Class Distribution')

plt.xticks(rotation=80)


plt.savefig('images/bar_chart.png')