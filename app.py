import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# PAGE CONFIG

st.set_page_config(
    page_title="Tele Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# LOAD MODEL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "data", "TeleCustomer_Churn_Model.pkl")

model = joblib.load(MODEL_PATH)

# TITLE

st.title("📊 Tele Customer Churn Prediction System")
st.markdown("Predict customer churn using the most important features.")

st.divider()

# INPUT SECTION

col1, col2 = st.columns(2)

with col1:

    tenure = st.slider(
        "Customer Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
    )

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

    Contract = st.selectbox(
        "Contract",
        [0, 1, 2]
    )

    InternetService = st.selectbox(
        "Internet Service",
        [0, 1, 2]
    )

with col2:

    OnlineSecurity = st.selectbox(
        "Online Security",
        [0, 1, 2]
    )

    TechSupport = st.selectbox(
        "Tech Support",
        [0, 1, 2]
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        [0, 1, 2]
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        [0, 1, 2, 3]
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        [0, 1]
    )

st.divider()

# PREDICT BUTTON

if st.button("🔮 Predict Churn", use_container_width=True):

    input_data = pd.DataFrame({

        'Contract': [Contract],
        'tenure': [tenure],
        'TotalCharges': [TotalCharges],
        'MonthlyCharges': [MonthlyCharges],
        'OnlineSecurity': [OnlineSecurity],
        'TechSupport': [TechSupport],
        'InternetService': [InternetService],
        'PaymentMethod': [PaymentMethod],
        'OnlineBackup': [OnlineBackup],
        'PaperlessBilling': [PaperlessBilling]

    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

    with metric2:
        st.metric(
            "Prediction",
            "Churn" if prediction == 1 else "No Churn"
        )

    st.progress(float(probability))

    if probability >= 0.70:
        st.error("🔴 High Churn Risk")

    elif probability >= 0.40:
        st.warning("🟡 Medium Churn Risk")

    else:
        st.success("🟢 Low Churn Risk")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to stay.")

# FOOTER
st.divider()
st.caption("Customer Churn Prediction using Random Forest Model")