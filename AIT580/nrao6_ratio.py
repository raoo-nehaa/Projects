# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:25:52 2024

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
    
    # Assuming a ratio column exists; replace 'Ratio_Column' with the actual name
ratio_column = 'id'  # Replace with a true ratio column if available
plt.figure(figsize=(8, 6))
df[ratio_column].dropna().plot(kind='hist', bins=20, color='green', edgecolor='black')
plt.title(f'Distribution of {ratio_column} (Ratio Data)', fontsize=14)
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()
