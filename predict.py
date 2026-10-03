from src.predictor import build_input, analyze_patient

print("=" * 55)
print("DISEASE RISK PREDICTION SYSTEM")
print("Type 2 Diabetes Risk Estimation")
print("=" * 55)

values = [
    float(input("Pregnancies: ")),
    float(input("Glucose (mg/dL): ")),
    float(input("Blood Pressure (mm Hg): ")),
    float(input("Skin Thickness (mm): ")),
    float(input("Insulin (mu U/mL): ")),
    float(input("BMI: ")),
    float(input("Diabetes Pedigree Function: ")),
    float(input("Age: ")),
]

patient = build_input(*values)
result = analyze_patient(patient)

print("\n" + "=" * 55)
print("PREDICTION RESULT")
print("=" * 55)
print(f"Estimated Risk Probability: {result['risk_probability']:.2%}")
print(f"Risk Level: {result['risk_level']}")
print(f"Priority: {result['priority']}")
print("Model Prediction: " + (
    "Higher-risk class" if result["prediction"] == 1 else "Lower-risk class"
))
print(f"Recommendation: {result['recommendation']}")
print("\nIMPORTANT: This is a machine-learning risk estimate, not a medical diagnosis.")
