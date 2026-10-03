import joblib
import pandas as pd

MODEL_PATH = "models/disease_risk_model.joblib"
model = joblib.load(MODEL_PATH)

def build_input(
    pregnancies, glucose, blood_pressure, skin_thickness,
    insulin, bmi, diabetes_pedigree, age
):
    return pd.DataFrame([{
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree": diabetes_pedigree,
        "age": age,
    }])

def risk_level(probability):
    if probability < 0.30:
        return "LOW"
    elif probability < 0.60:
        return "MODERATE"
    elif probability < 0.80:
        return "HIGH"
    return "VERY HIGH"

def analyze_patient(patient_data):
    probability = float(model.predict_proba(patient_data)[0][1])
    prediction = int(model.predict(patient_data)[0])
    risk = risk_level(probability)

    recommendations = {
        "LOW": (
            "The model estimates a lower diabetes risk. "
            "Continue healthy lifestyle practices and routine health monitoring."
        ),
        "MODERATE": (
            "The model estimates a moderate risk. "
            "Consider discussing the result and relevant risk factors with a qualified healthcare professional."
        ),
        "HIGH": (
            "The model estimates a higher risk. "
            "Consider professional medical evaluation and appropriate follow-up."
        ),
        "VERY HIGH": (
            "The model estimates a very high risk. "
            "Seek professional medical evaluation promptly. This prediction is not a diagnosis."
        ),
    }

    priority = {
        "LOW": "ROUTINE",
        "MODERATE": "MONITOR",
        "HIGH": "HIGH",
        "VERY HIGH": "URGENT REVIEW",
    }[risk]

    return {
        "risk_probability": probability,
        "prediction": prediction,
        "risk_level": risk,
        "priority": priority,
        "recommendation": recommendations[risk],
    }
