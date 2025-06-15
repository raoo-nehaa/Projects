# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:55:42 2024

@author: nehad
"""

import pandas as pd

# Load the Excel file
dataframe = 'C:/Users/nehad/Desktop/Courses/AIT/Finalproject/oomph CVII study cycle 3 - B2C Quant Data Set 2022.xlsx'  # Replace with the actual path
data = pd.read_excel(dataframe)

# View the first few rows
print(data.head())

# Check for missing values
print(data.isnull().mean()*100)

# View summary statistics
print(data.describe())

# Check column names
print(data.columns)

#Rename Columns
data.rename(columns={'OldColumnName': 'NewColumnName'}, inplace=True)

# Fill missing values with a default value
data.fillna('DefaultValue', inplace=True)


#Drop unnecessary columns
data.drop(['36. If you would like other forms of support from , please describe them in around 20 words below:'], axis=1, inplace=True)


#To save the clean dataset
output_path = 'C:/Users/nehad/Desktop/Courses/AIT/Finalproject/cleaned_dataset.xlsx'  # Replace with your desired path
data.to_excel(output_path, index=False)
print("Cleaned dataset saved to:", output_path)

