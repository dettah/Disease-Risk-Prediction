# Disease Risk Prediction AI

A machine-learning system for estimating type 2 diabetes risk using the Pima Indians Diabetes dataset.

## Important
This is an educational ML project. It estimates risk and is **not a medical diagnosis**.

## Workflow
Dataset → Cleaning → EDA → Feature Preparation → Scaling → Logistic Regression → Evaluation → Probability → Risk Category → Interface

## Features
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## Target
`outcome`
- 0 = lower-risk class in the dataset
- 1 = diabetes-positive class in the dataset

## Data Cleaning
Zero values in glucose, blood pressure, skin thickness, insulin, and BMI are treated as missing and replaced using the feature median.

## Why Logistic Regression?
It is a strong, interpretable baseline for binary classification and provides probabilities. Students can later compare it with Random Forest and XGBoost.

## Risk Categories
- <30%: LOW
- 30%–<60%: MODERATE
- 60%–<80%: HIGH
- 80%+: VERY HIGH

These are application-level categories, not clinical thresholds.

## Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/train.py
python predict.py
streamlit run app.py
```

## Presentation Questions
1. What problem does the system solve?
2. What is the target?
3. What does each feature mean?
4. Why are some zero values treated as missing?
5. Why use Logistic Regression?
6. Why is StandardScaler used?
7. What does the probability represent?
8. Why is recall important?
9. What are false positives and false negatives?
10. Why is this not a diagnosis?
11. What are the dataset limitations?
12. How could the model be improved?
