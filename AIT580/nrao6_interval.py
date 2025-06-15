# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:17:27 2024

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
    
    
# Plot interval data
interval_column = 'now_that_you_have_completed_this_stikky_exercise,_we’d_like_to_understand_what_factors_have_positively_or_negatively_changed_your_status_related_to_economic_or_wellbeing_factors_since_the_start_of_the_pandemic:'

# Clean the column: Remove or convert non-numeric values
df_cleaned = df.copy()

# Convert the column to numeric, invalid entries will become NaN
df_cleaned[interval_column] = pd.to_numeric(df_cleaned[interval_column], errors='coerce')

# Drop NaN values and plot the histogram
plt.figure(figsize=(8, 6))
df_cleaned[interval_column].dropna().plot(kind='hist', bins=20, color='orange', edgecolor='black')
plt.title(f'Distribution of {interval_column} (Interval Data)', fontsize=14)
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()


