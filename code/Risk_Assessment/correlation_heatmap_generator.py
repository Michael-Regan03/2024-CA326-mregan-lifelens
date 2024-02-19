import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#read file
df = pd.read_csv('balanced_data.csv')

#correlation matric
correlation_matrix = df.corr()



plt.figure(figsize=(12, 10))

#Remove repetition in top half
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))


#heatmap
sns.heatmap(correlation_matrix,mask=mask, annot=True, fmt=".2f", cmap='coolwarm')


plt.title('Behavioural Data Correlation with Chronic Ilness')


plt.savefig('images/correlation_heatmap.png')
