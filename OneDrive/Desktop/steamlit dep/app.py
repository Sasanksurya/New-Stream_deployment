import streamlit as st
import pandas as pd
import pickle
import traceback

# Load model safely
try:
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.code(traceback.format_exc())
    st.stop()

st.title("Loan Approval Prediction")

# Numerical inputs
ApplicantIncome = st.number_input("Applicant Income", min_value=0, value=5000)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0, value=0)
LoanAmount = st.number_input("Loan Amount", min_value=0, value=120)
Loan_Amount_Term = st.number_input("Loan Amount Term (months)", value=360)
Credit_History = st.selectbox("Credit History", [0.0, 1.0])

# Categorical inputs
Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Input dataframe
input_data = pd.DataFrame({
    "Gender": [Gender],
    "Married": [Married],
    "Dependents": [Dependents],
    "Education": [Education],
    "Self_Employed": [Self_Employed],
    "ApplicantIncome": [ApplicantIncome],
    "CoapplicantIncome": [CoapplicantIncome],
    "LoanAmount": [LoanAmount],
    "Loan_Amount_Term": [Loan_Amount_Term],
    "Credit_History": [Credit_History],
    "Property_Area": [Property_Area]
})

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")