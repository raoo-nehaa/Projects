# Chicago Public Library Event Analysis Using Statistical Methods

## Project Overview

This project leverages statistical analysis and machine learning to evaluate event-related data from the Chicago Public Library. The main objectives include predicting attendance, identifying key event features, and optimizing event planning. By using techniques such as linear regression, decision trees, and random forests, the study aims to provide insights that support better community engagement and data-driven event strategies.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Research Questions](#research-questions)
  - [Prediction of Insurance Costs](#prediction-of-insurance-costs)
  - [Shipment Classification](#shipment-classification)
  - [Delivery Outcome Prediction](#delivery-outcome-prediction)
- [Methodology](#methodology)
- [Results](#results)
- [Future Work](#future-work)


## Introduction

Effectively analyzing logistics data is essential for minimizing costs and enhancing operational efficiency. This study investigates the factors that impact insurance expenses in shipments, categorizes shipments based on insurance cost levels, and forecasts delivery outcomes using statistical modeling. The insights gained support informed decision-making in areas like risk assessment and process optimization.

## Dataset

The dataset includes a range of attributes related to shipment records, such as:

- **Shipping Details**: Mode of transport (air, sea, or road), origin country, and delivery dates.
- **Cost Data**: Freight charges (USD), insurance expenses (USD), and packaging prices.
- **Product Characteristics**: Category, sub-category, and dosage of the items shipped.
- **Operational Metrics**: Quantity and value of line items, along with shipment weight.

## Data Preprocessing

The dataset was thoroughly preprocessed with the following steps:

- Non-numeric entries in the **freight cost** and **weight columns** were converted into numeric values.
- Missing data points were filled using median imputation to address skewness in distributions.
- Categorical variables such as **shipment mode**, **country**, and **product group** were encoded for analysis.
- Outliers were removed through filtering based on percentile thresholds.
- New features were engineered, including **delivery_time**, calculated as the difference between scheduled and actual delivery dates.
- A **correlation matrix** was generated to examine the relationships among important variables.

## Research Questions

### Estimating Insurance Costs

- **Goal**: Determine the key factors influencing insurance cost estimation.
- **Methods**:
  - **Linear Regression**: Assessed the effects of variables like **line item value**, **freight cost**, and **shipment mode**.
  - **Random Forest**:Employed to better capture complex, non-linear patterns.
- **Outcomes**:
  - The line item value showed the strongest relationship with insurance costs.
  - The **Random Forest model (R² = 94.47%)** surpassed Linear Regression (R² = 92.64%) in predictive accuracy.

### Classifying Shipments by Insurance Cost

- **Goal**: Sort shipments into **low**, **medium**, and **high** insurance cost groups.
- **Methods:**
  - **Decision Tree**: Created classification rules from shipment features.
  - **Random Forest**: Enhanced classification performance using ensemble methods.
- **Outcomes:**
  - **Decision Tree Accuracy**: 93.87%
  - **Random Forest Accuracy**: 94.65%
  - Both models demonstrated strong precision and reliability in classification.

### Predicting Delivery Outcomes

- **Goal**:  Forecast whether shipments arrive **early**, **on-time**, or **late**.
- **Methods:**
  - **Logistic Regression**:  Identified key delivery performance drivers.
  - **Decision Tree & Random Forest**: Used to improve prediction accuracy.
- **Outcomes**:
  - Important predictors included pack price, delivery time, and line item value.
  - Achieved a model accuracy of 74.10%, indicating room for improvement.

## Methodology

1. **Feature Engineering**: Developed new variables like delivery time, insurance cost categories, and encoded categorical data.
2. **Exploratory Data Analysis (EDA)**: Utilized correlation matrices and visual tools to uncover trends.
3. **Model Selection**: Tested various algorithms (Linear Regression, Random Forest, Decision Tree, Logistic Regression) to identify the best predictors.
4. **Evaluation Metrics**: Assessed models using metrics such as R², RMSE, Accuracy, and Confusion Matrices.

## Results

- **Insurance Cost Prediction**: The Random Forest model delivered the highest accuracy.
- **Shipment Classification**:Both Decision Tree and Random Forest models effectively grouped shipments by insurance cost levels.
- **Delivery Outcome Prediction**: Key factors impacting delivery timing were identified, with the model reaching 74.10% accuracy.

## Future Work

- **Enhance Prediction Models**: Integrate advanced deep learning techniques like LSTM and Transformer architectures to improve results.
- **Broaden Feature Set**: Incorporate external influences such as weather conditions and economic indicators that affect delivery schedules.
- **Develop Real-Time Analytics**: Build dashboards for live monitoring of shipment patterns and cost fluctuations.
- **Optimize Logistics**: Leverage machine learning for dynamic, real-time supply chain decision-making.

