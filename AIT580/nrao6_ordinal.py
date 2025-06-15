# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:15:08 2024

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
    
# Frequency count for ordinal column
ordinal_column = 'help_with_cost_-_either_changed_payment_terms_or_reduced_price.'
ordinal_counts = df[ordinal_column].value_counts()

# Plot ordinal data
plt.figure(figsize=(8, 6))
ordinal_counts.plot(kind='bar', color='purple', edgecolor='black')
plt.title(f'Frequency of Responses in {ordinal_column} (Ordinal Data)', fontsize=14)
plt.xlabel('Response', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()
