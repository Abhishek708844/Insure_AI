import streamlit as st
from prediction_helper import predict

# Page Configuration
st.set_page_config(page_title="InsureAI", layout="wide")

st.title("🛡️ InsureAI - Health Insurance Cost Predictor")

st.markdown("""
Welcome to **InsureAI**. Enter your personal and health-related details below to get a prediction for your insurance cost.  
""")

st.divider()

# Create Expander for Inputs
with st.expander("🔧 Fill in your details", expanded=True):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider('🎂 Age', min_value=18, max_value=100, value=25)
        number_of_dependants = st.slider('👨‍👩‍👧‍👦 Number of Dependants', min_value=0, max_value=10, value=1)
        income_lakhs = st.slider('💰 Income (in Lakhs)', min_value=0, max_value=200, value=10)

    with col2:
        genetical_risk = st.slider('🧬 Genetical Risk Score (0 to 5)', min_value=0, max_value=5, value=2)
        insurance_plan = st.radio('📋 Insurance Plan', ['Bronze', 'Silver', 'Gold'], horizontal=True)
        employment_status = st.selectbox('💼 Employment Status', ['Salaried', 'Self-Employed', 'Freelancer', ''])

    with col3:
        gender = st.radio('⚧️ Gender', ['Male', 'Female'], horizontal=True)
        marital_status = st.selectbox('💍 Marital Status', ['Unmarried', 'Married'])
        region = st.selectbox('📍 Region', ['Northwest', 'Southeast', 'Northeast', 'Southwest'])

    bmi_category = st.radio('⚖️ BMI Category', ['Normal', 'Obesity', 'Overweight', 'Underweight'], horizontal=True)
    smoking_status = st.radio('🚬 Smoking Status', ['No Smoking', 'Regular', 'Occasional'], horizontal=True)
    medical_history = st.selectbox('🩺 Medical History', [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ])

# Prepare input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction Button
st.markdown("---")
if st.button("🧾 Predict Insurance Cost"):
    with st.spinner("Calculating..."):
        prediction = predict(input_dict)
        st.success(f"💡 Your Predicted Health Insurance Cost is: **₹{prediction:,}**")

