# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:08:39 2024

@author: nehad
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (make sure the path is correct)
df = pd.read_excel('C:\\Users\\nehad\\Desktop\\Courses\\AIT\\Finalproject\\cleaned_dataset.xlsx')

# Check the column names and their types
print(df.columns)

# Replace spaces in column names with underscores for easier access
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

for i in df.columns:
    print(i)


# Plot frequency of top 10 IDs
plt.figure(figsize=(8, 6))
df['id'].value_counts().head(10).plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Frequency of Top 10 IDs (Nominal Data)', fontsize=14)
plt.xlabel('ID', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()
