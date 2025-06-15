
# Impact of Bridge Design Materials and Climate Exposure on Deterioration and Condition
Course: AIT-614 –003 


## Project Overview

This project investigates how bridge design materials and climate conditions contribute to the deterioration of bridge structures. We use machine learning models to classify bridge conditions and draw insights from trends in structural design and geographic exposure.

The analysis and modeling are conducted using Python in a notebook-based environment.


## Dataset Details

- Main source: National Bridge Inventory (NBI) Dataset
- Additional attributes: Climate classification, structural material grouping, and derived deterioration indicators
- Preprocessed data files are integrated directly in the notebook. Raw datasets are available upon request.



## System Workflow

The system follows this structured pipeline:

1. Data Preparation
   - Cleans and merges bridge records with climate and material metadata.
   - Encodes categorical values and handles missing data.
   - Scales features for numerical consistency.

2. Exploratory Data Analysis
   - Visualizes condition ratings by design type, state, and climate zone.
   - Uses distribution plots and grouped summaries for interpretation.

3. Feature Engineering
   - Introduces custom features such as Climate Stress Zone and Material Category.
   - Identifies influential predictors based on domain knowledge and EDA.

4. Modeling
   - Models used: Logistic Regression, Random Forest, and XGBoost.
   - SMOTE is applied to address class imbalance in condition ratings.
   - Models are evaluated using accuracy, F1-score, and confusion matrices.

5. Outputs
   - Final outputs include performance summaries and visual comparisons of models.
   - Insights highlight material and environmental factors affecting bridge condition.


4. Notes

- SMOTE is implemented via `imblearn.over_sampling.SMOTE`.
- The notebook is fully self-contained, with each stage commented and described.
- If datasets are not accessible, please contact the project team or course staff.


