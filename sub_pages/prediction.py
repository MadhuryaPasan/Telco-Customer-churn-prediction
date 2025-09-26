import streamlit as st


def prediction_page():
    st.title("📋 Customer Details")
    st.write("Fill out the information below to predict churn:")

    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
            partner = st.selectbox("Partner", ["Yes", "No"])
            dependents = st.selectbox("Dependents", ["Yes", "No"])

        with col2:
            tenure = st.slider("Tenure (months)", 0, 72, 12)
            phone_service = st.selectbox("Phone Service", ["Yes", "No"])
            internet_service = st.selectbox(
                "Internet Service", ["DSL", "Fiber optic", "No"]
            )
            contract = st.selectbox(
                "Contract", ["Month-to-month", "One year", "Two year"]
            )

        with col3:
            payment_method = st.selectbox(
                "Payment Method",
                [
                    "Electronic check",
                    "Mailed check",
                    "Bank transfer (automatic)",
                    "Credit card (automatic)",
                ],
            )
            monthly_charges = st.number_input(
                "Monthly Charges ($)", min_value=0.0, value=50.0
            )
            total_charges = st.number_input(
                "Total Charges ($)", min_value=0.0, value=1000.0
            )

        submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        st.success(
            "✅ Prediction placeholder: Result will appear here (Churn / No Churn)."
        )
