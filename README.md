# Customer Retention & Churn Analysis

## Internship Project – Future Interns

### Project Overview

Customer retention is one of the most important business challenges in the telecom industry. Understanding customer behavior and identifying churn factors helps organizations improve customer satisfaction and reduce revenue loss.

This project focuses on analyzing telecom customer data, identifying churn-driving factors, creating interactive business dashboards, and building machine learning models capable of predicting customer churn.

The project combines Data Analysis, Business Intelligence, Machine Learning, Hyperparameter Tuning, Feature Importance Analysis, and Explainable AI techniques.

---

## Organization

**Future Interns**

### Domain

**Data Science & Machine Learning**

### Project Title

**Customer Retention & Churn Analysis**

---

## GitHub Repository

Repository Link:

**GitHub:**
https://github.com/Sanjayduduka45/FUTURE_DS02_Tele-Customer-Retention-Churn-Analysis.git

---

## Problem Statement

Customer churn directly impacts business growth and profitability. The objective of this project is to analyze customer retention patterns, identify factors responsible for customer attrition, and develop a predictive machine learning solution that can proactively identify customers at risk of leaving.

---

## Dataset Description

The dataset contains telecom customer information including:

* Customer ID
* Gender
* Senior Citizen Status
* Partner
* Dependents
* Contract Type
* Internet Service
* Payment Method
* Monthly Charges
* Total Charges
* Tenure
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming Services
* Churn Status

### Target Variable

**Churn**

* Yes → Customer Left Service
* No → Customer Retained Service

---

# Project Workflow

## 1. Data Cleaning & Preprocessing

Performed the following preprocessing steps:

* Missing value handling
* Data type corrections
* Duplicate record verification
* Feature selection
* Data preparation for machine learning
* Train-Test splitting

---

## 2. Exploratory Data Analysis (EDA)

Performed detailed analysis on:

* Churn Distribution
* Customer Demographics
* Contract Analysis
* Internet Service Analysis
* Payment Method Analysis
* Senior Citizen Analysis
* Gender Analysis
* Monthly Charges Distribution
* Tenure Analysis

---

## 3. Tableau Dashboard Development

Designed an interactive dashboard using Tableau Public.

### KPI Metrics

* Total Customers
* Churned Customers
* Active Customers
* Churn Rate

### Dashboard Visualizations

* Contract Analysis
* Payment Method Analysis
* Internet Service Analysis
* Senior Citizen vs Churn
* Gender Analysis

---

## 4. Machine Learning Model Development

Implemented multiple classification algorithms:

### Logistic Regression

Used as a baseline classification model.

### Random Forest Classifier

Implemented ensemble learning technique for improved prediction performance.

### XGBoost Classifier

Implemented gradient boosting model for churn prediction.

---

## 5. Hyperparameter Tuning

Optimized Random Forest using RandomizedSearchCV.

### Parameters Tuned

* n_estimators
* max_depth
* min_samples_split
* min_samples_leaf
* max_features
* class_weight

### Best Parameters

```python
{
'n_estimators': 800,
'min_samples_split': 5,
'min_samples_leaf': 4,
'max_features': 'log2',
'max_depth': 10,
'class_weight': 'balanced_subsample'
}
```

---

## 6. Model Evaluation

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

### Best Model

**Random Forest Classifier**

### Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 76.86% |
| Precision | 54.74% |
| Recall    | 74.06% |
| F1 Score  | 62.95% |
| ROC-AUC   | 84.53% |

---

## 7. Feature Importance Analysis

Top Important Features:

1. Contract
2. Tenure
3. Total Charges
4. Monthly Charges
5. Online Security
6. Tech Support
7. Internet Service
8. Payment Method
9. Online Backup
10. Paperless Billing

---

## 8. SHAP Explainability

Implemented SHAP (SHapley Additive Explanations) to understand model predictions.

### Benefits

* Improves model interpretability
* Identifies churn-driving features
* Explains feature impact on predictions
* Enhances business decision-making

---

# Business Insights

### Contract Analysis

* Month-to-month customers show the highest churn rate.
* Long-term contracts significantly reduce churn.

### Payment Method Analysis

* Electronic Check customers exhibit higher churn behavior.
* Automatic payment methods show better customer retention.

### Internet Service Analysis

* Fiber Optic customers have the highest churn count.
* Customers without internet service show lower churn.

### Senior Citizen Analysis

* Senior Citizens demonstrate relatively higher churn compared to non-senior customers.

### Gender Analysis

* Male and Female customers show similar churn behavior.

---

# Technologies Used

## Programming Language

* Python

## Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* SHAP
* Joblib

## Visualization Tool

* Tableau Public

## Development Tools

* Jupyter Notebook
* VS Code

---

# Project Structure

```text
FUTURE_DS02_Tele-Customer-Retention-Churn-Analysis/
│
├── Cleaned_Customer_Churn.csv
├── Customer_churn.ipynb
├── Churn_Prediction_Model.ipynb
├── TeleCustomer_Churn_Model.pkl
├── app.py
├── README.md
│
└── Tableau Dashboard Files
```

---

# Future Improvements

* Flask Deployment
* Streamlit Web Application
* Real-Time Prediction System
* Automated Model Retraining
* Cloud Deployment
* Customer Retention Recommendation Engine

---

# Conclusion

This project successfully analyzes telecom customer retention patterns and predicts customer churn using machine learning techniques. The Random Forest model achieved strong predictive performance with a ROC-AUC score of 84.53%.

The project provides valuable business insights that can help telecom companies identify high-risk customers and implement effective retention strategies.

---

# Internship Information

### Organization

Future Interns

