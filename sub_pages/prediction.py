import streamlit as st
from helper.frontend_inputs import *
from helper.churn_prediction import *


def prediction_page():
    
    page_bg = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    body {{
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #e0f7ff, #a1c4fd, #ffffff);
        color: #000000;
    }}

    .footer {{
        text-align: center;
        color: #000000;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align: center;'>Telco Customer Churn Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Fill out the information below to predict churn:</p>", unsafe_allow_html=True)
    st.markdown("---") 

    with st.form("prediction_form"):
      

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

        st.toast("✅ Prediction successful! Review the result below.")

        # --- Main Result Display ---
        if prediction == 1:
            # High Risk Card
            st.markdown(
                """
                <div style='background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); 
                            padding: 2rem; border-radius: 15px; margin-bottom: 1.5rem;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                    <h1 style='color: white; margin: 0; font-size: 2rem;'>
                        🚨 High Churn Risk Detected
                    </h1>
                    <p style='color: rgba(255,255,255,0.95); font-size: 1.2rem; margin-top: 0.5rem;'>
                        This customer is likely to leave soon
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Action Items
            st.markdown("### 🎯 Recommended Actions")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(
                    """
                    <div style='background-color: #fff3cd; padding: 1.2rem; 
                                border-radius: 10px; border-left: 4px solid #ffc107;'>
                        <h4 style='margin-top: 0; color: #856404;'>📞 Contact Customer</h4>
                        <p style='color: #856404; margin-bottom: 0;'>
                            Reach out proactively to understand concerns
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            with col2:
                st.markdown(
                    """
                    <div style='background-color: #d1ecf1; padding: 1.2rem; 
                                border-radius: 10px; border-left: 4px solid #17a2b8;'>
                        <h4 style='margin-top: 0; color: #0c5460;'>🎁 Retention Offer</h4>
                        <p style='color: #0c5460; margin-bottom: 0;'>
                            Consider special pricing or service upgrade
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
        else:
            # Low Risk Card
            st.markdown(
                """
                <div style='background: linear-gradient(135deg, #51cf66 0%, #37b24d 100%); 
                            padding: 2rem; border-radius: 15px; margin-bottom: 1.5rem;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                    <h1 style='color: white; margin: 0; font-size: 2rem;'>
                        ✅ Low Churn Risk
                    </h1>
                    <p style='color: rgba(255,255,255,0.95); font-size: 1.2rem; margin-top: 0.5rem;'>
                        This customer is predicted to stay
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Success Actions
            st.markdown("### 💡 Keep Them Happy")
            st.markdown(
                """
                <div style='background-color: #d4edda; padding: 1.2rem; 
                            border-radius: 10px; border-left: 4px solid #28a745;'>
                    <p style='color: #155724; margin: 0; font-size: 1.05rem;'>
                        <strong>Continue excellent service</strong> and maintain regular engagement 
                        to ensure this customer remains satisfied.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # --- Probability Visual Display ---
        st.markdown("### 📊 Confidence Level")

        # Create a visual progress bar for probability
        col1, col2 = st.columns([3, 1])

        with col1:
            # Determine color based on risk level
            if probability >= 0.7:
                bar_color = "#dc3545"  # Red
                risk_label = "Very High Risk"
            elif probability >= 0.5:
                bar_color = "#fd7e14"  # Orange
                risk_label = "High Risk"
            elif probability >= 0.3:
                bar_color = "#ffc107"  # Yellow
                risk_label = "Moderate Risk"
            else:
                bar_color = "#28a745"  # Green
                risk_label = "Low Risk"
            
            st.markdown(
                f"""
                <div style='background-color: #e9ecef; border-radius: 10px; 
                            padding: 0.5rem; margin-bottom: 1rem;'>
                    <div style='background-color: {bar_color}; width: {probability*100}%; 
                                height: 30px; border-radius: 8px; 
                                display: flex; align-items: center; justify-content: center;
                                transition: width 0.3s ease;'>
                        <span style='color: white; font-weight: bold; font-size: 0.9rem;'>
                            {probability:.1%}
                        </span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.metric("Churn Probability", f"{probability:.1%}", risk_label)

        # Simple explanation without technical jargon
        st.markdown(
            f"""
            <div style='background-color: #f8f9fa; padding: 1rem; 
                        border-radius: 10px; margin-top: 1rem;'>
                <p style='margin: 0; color: #495057; font-size: 0.95rem;'>
                    <strong>What this means:</strong> Our prediction model analyzed this customer's 
                    behavior and estimates a <strong>{probability:.1%}</strong> likelihood of churn. 
                    {f"This exceeds our {threshold:.0%} alert threshold, triggering a high-risk classification." if prediction == 1 
                    else f"This is below our {threshold:.0%} alert threshold, indicating the customer is likely to stay."}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Footer
        st.markdown(
            "<div class='footer'>"
            "Built with  by RuleQuest | Telco Customer Churn Prediction Project | "
            "Driving Customer Retention Through AI Innovation"
            "</div>",
            unsafe_allow_html=True,
        )