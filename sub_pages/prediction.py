import streamlit as st
from helper.frontend_inputs import *
from helper.churn_prediction import *


def prediction_page():
    st.title("📋 Customer Details")
    st.write("Fill out the information below to predict churn:")

    with st.form("prediction_form"):
        st.header("📊 Telco Customer Churn Prediction")

        # --- Customer Info ---
        st.subheader("👤 Customer Information")
        col1, col2 = st.columns(2)
        with col1:
            gender = st.selectbox("Gender", ["Male", "Female", "Unknown"])
            senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
            partner = st.selectbox("Partner", ["Yes", "No", "Unknown"])
            dependents = st.selectbox("Dependents", ["Yes", "No", "Unknown"])
            tenure_value = st.slider("Tenure (months)", 0, 72, 12)

        with col2:
            phone_service = st.selectbox("Phone Service", ["Yes", "No"])
            multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "Unknown"])
            phone_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
            internet_service = st.selectbox(
                "Internet Service", ["DSL", "Fiber optic", "No"]
            )
            contract_value = st.selectbox(
                "Contract", ["Month-to-Month", "One year", "Two year"]
            )

        st.markdown("---")

        # --- Services ---
        st.subheader("💻 Services Subscribed")
        col3, col4 = st.columns(2)
        with col3:
            online_security = st.selectbox("Online Security", ["Yes", "No", "Unknown"])
            online_backup = st.selectbox("Online Backup", ["Yes", "No", "Unknown"])
            device_protection = st.selectbox(
                "Device Protection", ["Yes", "No", "Unknown"]
            )

        with col4:
            tech_support = st.selectbox("Tech Support", ["Yes", "No", "Unknown"])
            streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "Unknown"])
            streaming_movies = st.selectbox(
                "Streaming Movies", ["Yes", "No", "Unknown"]
            )

        st.markdown("---")

        # --- Billing ---
        st.subheader("💳 Billing & Payment")
        col5, col6 = st.columns(2)
        with col5:
            payment_method = st.selectbox(
                "Payment Method",
                [
                    "Electronic check",
                    "Mailed check",
                    "Bank transfer (automatic)",
                    "Credit card (automatic)",
                    "Unknown",
                ],
            )

        with col6:
            monthly_charges = st.number_input(
                "Monthly Charges ($)", min_value=0.0, value=50.0
            )
            total_charges = monthly_charges * tenure_value
            st.text_input("Total Charges ($)", value=total_charges, disabled=True)

        st.markdown("---")

        # --- Submit ---
        submitted = st.form_submit_button("🔍 Predict", width="stretch")

    if submitted:
        gender_Female, gender_Unknown = gender_conv(gender)
        SeniorCitizen = senior_citizen_conv(senior_citizen)
        Partner_No, Partner_Unknown, Partner_Yes = partner_conv(partner)
        Dependents_No, Dependents_Unknown, Dependents_Yes = dependents_conv(dependents)
        MultipleLines_No, MultipleLines_Unknown, MultipleLines_Yes = (
            multiple_lines_conv(multiple_lines)
        )

        OnlineSecurity_No, OnlineSecurity_Unknown, OnlineSecurity_Yes = (
            online_security_conv(online_security)
        )
        OnlineBackup_No, OnlineBackup_Unknown, OnlineBackup_Yes = online_backup_conv(
            online_backup
        )
        DeviceProtection_No, DeviceProtection_Unknown, DeviceProtection_Yes = (
            device_protection_conv(device_protection)
        )
        TechSupport_No, TechSupport_Unknown, TechSupport_Yes = tech_support_conv(
            tech_support
        )
        StreamingTV_No, StreamingTV_Unknown, StreamingTV_Yes = streaming_tv_conv(
            streaming_tv
        )
        StreamingMovies_No, StreamingMovies_Unknown, StreamingMovies_Yes = (
            streaming_movies_conv(streaming_movies)
        )

        tenure = tenure_conv(tenure_value)
        PhoneService = phone_service_conv(phone_service)
        PaperlessBilling = phone_billing_conv(phone_billing)
        InternetService_DSL, InternetService_Fiber_optic, InternetService_No = (
            internet_service_conv(internet_service)
        )
        Contract_Month_to_Month, Contract_One_year, Contract_Two_year = (
            contract_value_conv(contract_value)
        )
        (
            PaymentMethod_Bank_transfer_automatic,
            PaymentMethod_CreditP_card_automatic,
            PaymentMethod_Electronic_check,
            PaymentMethod_Mailed_check,
            PaymentMethod_Unknown,
        ) = payment_method_conv(payment_method)
        MonthlyCharges, TotalCharges = monthly_total_charges_conv(
            monthly_charges, total_charges
        )
        customer_features = [
            SeniorCitizen,
            tenure,
            PhoneService,
            PaperlessBilling,
            MonthlyCharges,
            TotalCharges,
            Contract_Month_to_Month,
            Contract_One_year,
            Contract_Two_year,
            PaymentMethod_Bank_transfer_automatic,
            PaymentMethod_CreditP_card_automatic,
            PaymentMethod_Electronic_check,
            PaymentMethod_Mailed_check,
            PaymentMethod_Unknown,
            gender_Female,
            gender_Unknown,
            Partner_No,
            Partner_Unknown,
            Partner_Yes,
            Dependents_No,
            Dependents_Unknown,
            Dependents_Yes,
            MultipleLines_No,
            MultipleLines_Unknown,
            MultipleLines_Yes,
            InternetService_DSL,
            InternetService_Fiber_optic,
            InternetService_No,
            OnlineSecurity_No,
            OnlineSecurity_Unknown,
            OnlineSecurity_Yes,
            OnlineBackup_No,
            OnlineBackup_Unknown,
            OnlineBackup_Yes,
            DeviceProtection_No,
            DeviceProtection_Unknown,
            DeviceProtection_Yes,
            TechSupport_No,
            TechSupport_Unknown,
            TechSupport_Yes,
            StreamingTV_No,
            StreamingTV_Unknown,
            StreamingTV_Yes,
            StreamingMovies_No,
            StreamingMovies_Unknown,
            StreamingMovies_Yes,
        ]

        # prediction, probability, threshold ,class_label = predict_new_customer_churn_mlp(
        #     customer_data=customer_features, threshold=0.5
        # )
        prediction, probability, threshold ,class_label = predict_new_customer_churn_LogisticRegression(
            customer_data=customer_features, threshold=0.5
        )

        st.toast("✅ Prediction is successful")
        st.success(
            f"Prediction: **{prediction}** **`({class_label})`**")

        # st.markdown(
        #     f"""
        #     ---
        #     **Details**
        #     * Probability: `{probability:.4f}`
        #     * Threshold Used: `{threshold}`
        #     """
        # )
        
        # Add the interpretation of the prediction
        if prediction == 1:
            st.info("⚠️ **Action Recommended:** This customer is predicted to **Churn**.")
        else:
            st.info("✅ **Good News:** This customer is predicted to **NOT Churn**.")

        st.markdown("---")

        # 2. Details Section (Existing Code with minor formatting adjustments)
        st.markdown(
            f"""
            **Details**
            * **Probability:** `{probability:.4f}`
            * **Threshold Used:** `{threshold}`
            """
        )

        # 3. Interpretation of Probability and Threshold (New Details)
        st.markdown("---")
        st.markdown(
            """
            ### Interpretation
            """
        )

        # Detail 3a: Explain the Probability
        st.markdown(
            f"""
            The model estimates a **{probability:.2%}** probability that this customer will churn.
            """
        )

        # Detail 3b: Explain the decision logic
        st.markdown(
            f"""
            Since the predicted probability of **{probability:.4f}** is **{'greater' if probability > threshold else 'less'}** than the decision threshold of **{threshold}**, the final classification is **`{class_label}`**.
            """
        )
        st.markdown("---")
