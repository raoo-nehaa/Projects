# Movie Recommendation System

##  Introduction
In today's data-driven world, recommendation systems enhance user experiences across industries. This project builds a **movie recommendation system** using two powerful approaches:  
- **K-Nearest Neighbors (KNN)**  
- **Collaborative Filtering (CF)**  

The goal is to provide personalized movie suggestions by analyzing user ratings and leveraging similarity metrics. The pipeline includes data cleaning, exploratory data analysis (EDA), model development, and performance evaluation.

---

## Data Preprocessing & EDA

### Missing Value Handling
- Checked for missing values in `rating`, `rating_user_id`, and `movieId`.
- Applied imputation or dropped incomplete rows to maintain data quality.

### Exploratory Data Analysis (EDA)
- **Rating Distribution**: Histograms used to explore how users rate movies.
- **Popular Movies**: Bar plots of most/least rated movies.
- **User Activity**: Scatter plots analyzed correlation between number of ratings and average score.

---

##  Methods

###  1. K-Nearest Neighbors (KNN)

####  Process:
- **Unweighted KNN**: Average rating from `k` nearest users.
- **Weighted KNN**: Weighted average, inversely proportional to user distances.
- Used **Euclidean distance** as the similarity metric.

####  Evaluation:
- RMSE used to compare actual vs. predicted ratings.

####  Results:
| Method            | K = 3 | K = 5 | K = 10 |
|-------------------|-------|-------|--------|
| Unweighted KNN    | 1.0741 | 1.0269 | **0.9946** |
| Weighted KNN      | 1.1175 | 1.0801 | 1.0515  |

####  Inference:
- RMSE improves with increasing `k`.
- **Unweighted KNN consistently outperforms** the weighted version.
- Best config: **Unweighted KNN, k = 10** (RMSE = 0.9946)

---

###  2. Collaborative Filtering (CF)

####  Process:
- Averaged duplicate user-movie ratings.
- Split data into train/test (60:40, 70:30, 80:20).
- Created a **utility matrix** (users × movies).
- Applied **zero-centering** on movie ratings.
- Used **Pearson correlation** for movie similarity.
- Predicted ratings via weighted average of rated similar movies.

####  Results:
| Train-Test Split | RMSE     |
|------------------|----------|
| 60-40            | 1.1918   |
| 70-30            | 1.1538   |
| 80-20            | **1.1307** |

####  Inference:
- Accuracy improves with more training data.
- Suffers from **cold start** and **sparsity** issues.

---

##  Requirements

Install the following Python packages before running the notebook:

pip install numpy pandas matplotlib seaborn scikit-learn
