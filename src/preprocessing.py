import pandas as pd
import numpy as np

ZERO_AS_MISSING = [
    "glucose", "blood_pressure", "skin_thickness", "insulin", "bmi"
]

NUMERICAL_COLUMNS = [
    "pregnancies", "glucose", "blood_pressure", "skin_thickness",
    "insulin", "bmi", "diabetes_pedigree", "age"
]

def clean_data(df):
    df = df.copy()
    for column in ZERO_AS_MISSING:
        df[column] = df[column].replace(0, np.nan)
        df[column] = df[column].fillna(df[column].median())
    return df

def prepare_features(df):
    df = clean_data(df)
    X = df[NUMERICAL_COLUMNS].copy()
    y = df["outcome"].astype(int)
    return X, y
