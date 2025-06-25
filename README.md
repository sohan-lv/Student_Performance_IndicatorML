# Student Performance Analysis using ML

This project analyzes how various demographic and educational factors impact student performance in standardized exams. It combines exploratory data analysis (EDA) and machine learning modeling to identify patterns and make performance predictions.

---

## Problem Statement

The objective is to understand how a student's test scores are influenced by factors such as:
- Gender
- Ethnicity
- Parental level of education
- Lunch type
- Test preparation course

---

## Project Structure

1. **EDA Notebook**  
   - Univariate & bivariate analysis using seaborn and matplotlib  
   - Correlation heatmaps and distribution plots  
   - Insights into how features relate to performance in different subjects

2. **Model Training Notebook**  
   - Preprocessed features for regression modeling  
   - Algorithms used:
     - Linear Regression, Decision Tree, Random Forest, XGBoost, CatBoost, AdaBoost
   - Model evaluation using MAE, MSE, and R² score

---

## Key Insights

- Students who completed test preparation consistently performed better.
- Parental education level shows a positive correlation with student scores.
- Female students scored higher in reading and writing on average, while math scores were balanced.

---

## Tech Stack

- **Languages & Tools:** Python, Pandas, NumPy, Seaborn, Matplotlib
- **ML Models:** Scikit-learn, XGBoost, CatBoost
- **Evaluation Metrics:** MAE, RMSE, R²

---

## How to Run

1. Clone this repo
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Run notebooks:  
   Open `.ipynb` files in Jupyter or VS Code

