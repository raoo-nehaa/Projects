# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:07:17 2024

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

# Selecting relevant columns
relevant_data = df[
    [
        "8._choose_one_option_that_best_describes_your_ethnic_group_or_background.",
        "help_with_understanding_pandemic_related_policies_and_practice."
    ]
].dropna()

# Renaming columns for convenience
relevant_data.columns = ["Ethnic_Group", "Satisfaction_Level"]

# Summary statistics
print(relevant_data.groupby("Ethnic_Group")["Satisfaction_Level"].value_counts())

# Visualizing the distribution
plt.figure(figsize=(12, 6))
sns.countplot(
    data=relevant_data, 
    y="Ethnic_Group", 
    hue="Satisfaction_Level", 
    palette="Set2"
)
plt.title("Satisfaction Level with Pandemic Policies by Ethnic Group")
plt.xlabel("Count")
plt.ylabel("Ethnic Group")
plt.legend(title="Satisfaction Level", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
