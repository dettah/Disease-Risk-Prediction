import streamlit as st
from src.predictor import build_input, analyze_patient

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Diabetes Risk Assessment",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# STYLES – Clean, clinical, restrained
# ============================================================
st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: #f8fafc;
    color: #0f172a;
}

.main .block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* ---------- Header ---------- */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 1.25rem;
    border-bottom: 1px solid #e2e8f0;
    margin-bottom: 2rem;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 12px;
}

.header-icon {
    width: 36px;
    height: 36px;
    background: #0f172a;
    color: white;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
}

.header-title {
    font-size: 16px;
    font-weight: 600;
    color: #0f172a;
    letter-spacing: -0.2px;
}

.header-subtitle {
    font-size: 12px;
    color: #64748b;
    margin-top: 1px;
}

.header-meta {
    font-size: 12px;
    color: #64748b;
}

/* ---------- Page title ---------- */
.page-title {
    font-size: 24px;
    font-weight: 600;
    color: #0f172a;
    letter-spacing: -0.4px;
    margin-bottom: 6px;
}

.page-description {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
    max-width: 640px;
    margin-bottom: 1.75rem;
}

/* ---------- Alert / Disclaimer ---------- */
.alert {
    background: #f1f5f9;
    border-left: 3px solid #64748b;
    padding: 12px 16px;
    font-size: 13px;
    color: #334155;
    line-height: 1.55;
    margin-bottom: 2rem;
}

/* ---------- Section ---------- */
.section-title {
    font-size: 13px;
    font-weight: 600;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 12px;
}

/* ---------- Form container ---------- */
.form-container {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 24px 24px 16px 24px;
    margin-bottom: 1.5rem;
}

/* ---------- Inputs ---------- */
label {
    color: #334155 !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

div[data-baseweb="input"] {
    border-radius: 6px !important;
}

/* ---------- Button ---------- */
div.stButton > button {
    background: #0f172a;
    color: white;
    border: none;
    border-radius: 6px;
    height: 42px;
    font-weight: 500;
    font-size: 14px;
    transition: background 0.15s ease;
}

div.stButton > button:hover {
    background: #1e293b;
    border: none;
    color: white;
}

/* ---------- Results ---------- */
.results-header {
    font-size: 15px;
    font-weight: 600;
    color: #0f172a;
    margin: 2rem 0 1rem 0;
    padding-bottom: 8px;
    border-bottom: 1px solid #e2e8f0;
}

.results-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 1.25rem;
}

.result-item {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 16px;
}

.result-label {
    font-size: 11px;
    font-weight: 500;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 6px;
}

.result-value {
    font-size: 22px;
    font-weight: 600;
    color: #0f172a;
    letter-spacing: -0.3px;
}

.result-note {
    font-size: 12px;
    color: #94a3b8;
    margin-top: 4px;
}

/* Classification */
.classification {
    padding: 12px 16px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
    margin-bottom: 1rem;
}

.classification.high {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    color: #9a3412;
}

.classification.low {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    color: #166534;
}

/* Recommendation */
.recommendation {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 16px 18px;
}

.recommendation-label {
    font-size: 12px;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 6px;
}

.recommendation-text {
    font-size: 14px;
    color: #334155;
    line-height: 1.6;
}

/* Model note */
.model-note {
    font-size: 12px;
    color: #94a3b8;
    margin-top: 1rem;
    line-height: 1.5;
}

/* Footer */
.footer {
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px solid #e2e8f0;
    font-size: 12px;
    color: #94a3b8;
    text-align: center;
}

/* Mobile */
@media (max-width: 768px) {
    .results-grid {
        grid-template-columns: 1fr;
    }
    .header {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }
}
</style>
""")

# ============================================================
# HEADER
# ============================================================
st.html("""
<div class="header">
    <div class="header-left">
        <div class="header-icon">🩺</div>
        <div>
            <div class="header-title">Diabetes Risk Assessment</div>
            <div class="header-subtitle">Clinical decision support tool</div>
        </div>
    </div>
    <div class="header-meta">Research use only</div>
</div>
""")

# ============================================================
# PAGE INTRO
# ============================================================
st.html("""
<div class="page-title">Type 2 Diabetes Risk Estimation</div>
<div class="page-description">
    Enter available patient measurements to obtain a model-based risk estimate.
    This tool is intended for educational and research purposes only.
</div>
""")

st.html("""
<div class="alert">
    This is a machine-learning estimate, not a clinical diagnosis.
    Results should always be interpreted by a qualified healthcare professional
    in the context of the full clinical picture.
</div>
""")

# ============================================================
# INPUT FORM
# ============================================================
st.html('<div class="section-title">Patient Measurements</div>')

with st.container(border=True):
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        pregnancies = st.number_input("Number of pregnancies", min_value=0, max_value=20, value=1, step=1)
        glucose = st.number_input("Plasma glucose (mg/dL)", min_value=0.0, max_value=300.0, value=120.0)
        blood_pressure = st.number_input("Diastolic blood pressure (mm Hg)", min_value=0.0, max_value=200.0, value=70.0)
        skin_thickness = st.number_input("Triceps skin fold thickness (mm)", min_value=0.0, max_value=100.0, value=20.0)

    with col2:
        insulin = st.number_input("2-Hour serum insulin (mu U/mL)", min_value=0.0, max_value=900.0, value=80.0)
        bmi = st.number_input("Body mass index (BMI)", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
        diabetes_pedigree = st.number_input("Diabetes pedigree function", min_value=0.0, max_value=3.0, value=0.5, step=0.01, format="%.3f")
        age = st.number_input("Age (years)", min_value=1, max_value=120, value=30, step=1)

    st.write("")  # small spacer
    analyze = st.button("Run Risk Assessment", type="primary", use_container_width=True)

# ============================================================
# RESULTS
# ============================================================
if analyze:
    patient = build_input(
        pregnancies, glucose, blood_pressure, skin_thickness,
        insulin, bmi, diabetes_pedigree, age
    )
    result = analyze_patient(patient)

    st.html('<div class="results-header">Assessment Results</div>')

    # Metrics row
    st.html(f"""
    <div class="results-grid">
        <div class="result-item">
            <div class="result-label">Estimated Probability</div>
            <div class="result-value">{result['risk_probability']:.1%}</div>
            <div class="result-note">Model output</div>
        </div>
        <div class="result-item">
            <div class="result-label">Risk Category</div>
            <div class="result-value">{result['risk_level']}</div>
            <div class="result-note">Application-defined</div>
        </div>
        <div class="result-item">
            <div class="result-label">Priority</div>
            <div class="result-value">{result['priority']}</div>
            <div class="result-note">Based on model output</div>
        </div>
    </div>
    """)

    # Classification
    if result["prediction"] == 1:
        st.html("""
        <div class="classification high">
            The model assigned this case to the higher-risk class.
        </div>
        """)
    else:
        st.html("""
        <div class="classification low">
            The model assigned this case to the lower-risk class.
        </div>
        """)

    # Recommendation
    st.html(f"""
    <div class="recommendation">
        <div class="recommendation-label">Suggested next step</div>
        <div class="recommendation-text">{result['recommendation']}</div>
    </div>
    """)

    st.html("""
    <div class="model-note">
        Probability is produced by the trained model. Risk categories are application-level
        labels and should not be treated as validated clinical thresholds.
    </div>
    """)

# ============================================================
# FOOTER
# ============================================================
st.html("""
<div class="footer">
    For research and educational use only · Not a medical device · 
    Always combine with clinical judgment
</div>
""")