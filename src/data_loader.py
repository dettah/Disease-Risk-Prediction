import os
import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

COLUMN_NAMES = [
    "pregnancies", "glucose", "blood_pressure", "skin_thickness",
    "insulin", "bmi", "diabetes_pedigree", "age", "outcome"
]

def load_dataset(save_path="data/pima_indians_diabetes.csv"):
    df = pd.read_csv(DATA_URL, header=None, names=COLUMN_NAMES)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    return df
