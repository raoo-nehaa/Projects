# Patient Matching and Master Patient Index (MPI) Analysis

## Project Overview

This project, completed for **HAP720-001: Data Integration Project - Phase 3**, evaluates the effectiveness of patient matching techniques and contrasts them with the potential advantages of using a Master Patient Index (MPI). The goal is to assess data linkage accuracy and highlight the challenges inherent in healthcare data integration.
  
##  Objectives

- Compare match and mismatch records using patient matching techniques
- Discuss performance implications if MPI were available
- Identify data quality issues and challenges in matching accuracy
- Recommend improvements for real-world healthcare integration

##  Dataset(s)

The analysis was performed on anonymized patient data files with demographic and clinical variables such as:

- Patient identifiers  
- Gender  
- Age  
- Diagnosis (ICD) codes  

> **Note:** Actual dataset files are not included in the GitHub repo due to privacy policies.

##  Tools & Technologies

| Tool        | Purpose                        |
|-------------|-------------------------------|
| **Python (Pandas)** | Data wrangling and matching logic |
| **Jupyter Notebook** | Interactive implementation and testing |
| **CSV/XLSX** | Input datasets for comparison |

## Methodology

1. **Data Preprocessing**
   - Normalized demographic fields (e.g., converting "M" ↔ "Male")
   - Cleaned ICD codes
   - Handled missing values

2. **Exact Patient Matching**
   - Based on age, gender, and diagnosis
   - Performed row-wise record comparisons

3. **Performance Metrics**
   - **Matched Records:** `1,110,886`  
   - **Mismatched Records:** `3,079,264`

4. **MPI Comparison (Theoretical)**
   - MPI expected to **reduce mismatches** via unique patient identifiers
   - More resilient to formatting differences and minor data variations

##  Challenges Identified

- Inconsistent data formatting (e.g., gender and ICD code variations)
- Typographical and missing values
- Real-world changes in patient demographics over time
- Rigid matching criteria leading to avoidable mismatches

## Key Takeaways

- MPI could significantly improve match rates and reduce manual reconciliation
- Advanced matching algorithms and standardization are critical for scalable health data integration
- Proper data governance and interoperability standards are essential for patient safety and system efficiency


