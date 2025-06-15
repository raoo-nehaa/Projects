create schema finalproject;
use finalproject;
Drop Table customer_feedback_data;
CREATE TABLE customer_feedback_data (
    id INT PRIMARY KEY,
    sector VARCHAR(50),
    residing_in_uk BOOLEAN,
    screening_question BOOLEAN,
    most_used_service VARCHAR(100),
    age_range VARCHAR(20),
    gender VARCHAR(20),
    ethnic_group VARCHAR(100),
    household_status VARCHAR(100),
    annual_income VARCHAR(50),
    income_impact VARCHAR(50),
    location VARCHAR(50),
    buying_behavior_change TEXT,
    return_to_pre_habits VARCHAR(10),
    customer_feedback_impact TEXT,
    vaccination_status VARCHAR(100),
    covid_impact_on_services TEXT,
    support_helpfulness TEXT
);

INSERT INTO customer_feedback_data (
    id, sector, residing_in_uk, screening_question, most_used_service, age_range, gender, ethnic_group,
    household_status, annual_income, income_impact, location, buying_behavior_change,
    return_to_pre_habits, customer_feedback_impact, vaccination_status, covid_impact_on_services,
    support_helpfulness
)
VALUES
(1, 'Automotive', TRUE, TRUE, 'Audi', '55 - 64', 'Female', 'White',
 'Shared adult household', '£50,000 to £74,999', 'Positively', 'England',
 'Wholesale change - my buying behaviour is completely different', 'No', 'Positive impact - the products/services have become more important and accessible to you.', 'I\'ve had both jabs and the booster', 'Positive impact', 'Extremely helpful'),
(2, 'Automotive', TRUE, TRUE, 'BMW', '45 - 54', 'Female', 'White',
 'Parents with school-age children', '£50,000 to £74,999', 'Positively', 'England',
 'Moderate change - I have changed some areas of my buying behaviour', 'No', 'Positive impact - the products/services have become more important and accessible to you.', 'I\'ve had both jabs and the booster', 'Positive impact', 'Somewhat helpful');

-- Query to analyze feedback Impact
WITH FeedbackAnalysis AS (
    SELECT
        buying_behavior_change,
        return_to_pre_habits,
        CASE
            WHEN customer_feedback_impact LIKE '%Positive%' THEN 'Positive Feedback'
            WHEN customer_feedback_impact LIKE '%Negative%' THEN 'Negative Feedback'
            ELSE 'Neutral Feedback'
        END AS feedback_category
    FROM customer_feedback_data
)
SELECT
    feedback_category,
    COUNT(*) AS total_responses,
    AVG(CASE WHEN buying_behavior_change LIKE '%Wholesale%' THEN 1 ELSE 0 END) * 100 AS percent_wholesale_change,
    AVG(CASE WHEN return_to_pre_habits = 'Yes' THEN 1 ELSE 0 END) * 100 AS percent_return_to_pre_habits
FROM FeedbackAnalysis
GROUP BY feedback_category;
