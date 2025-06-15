# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:01:33 2024

@author: nehad
"""

# 1) What differences exist in customer satisfaction amongst B2C product categories?

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel('C:\\Users\\nehad\\Desktop\\Courses\\AIT\\Finalproject\\cleaned_dataset.xlsx')
# Check the first few rows to confirm successful loading
print(data.head())


# Replace spaces in column names with underscores for easier access
data.columns = data.columns.str.strip().str.replace(' ', '_').str.lower()
for i in data.columns:
    print(i)
    print()# Check updated column names


# Rename column for convenience
satisfaction_column = "help_with_cost_-_either_changed_payment_terms_or_reduced_price."

# Create a count of satisfaction levels grouped by Sector
satisfaction_counts = data.groupby(['sector', satisfaction_column]).size().unstack()

# Plot the data as a bar chart
satisfaction_counts.plot(kind='bar', figsize=(10, 6), stacked=True)

# Add labels and title
plt.title('Customer Satisfaction Levels by Sector')
plt.xlabel('Sector')
plt.ylabel('Count of Responses')
plt.legend(title='Satisfaction Level', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()
