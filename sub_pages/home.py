import streamlit as st 

def home_page():
    st.title("📊 Telco Customer Churn Prediction")
    st.subheader("Welcome to the Customer Churn Prediction System")
    st.write(
        """
    This app helps telecom companies predict whether a customer is likely to **churn** 
    based on various factors like demographics, services used, and billing information.
    
    Use the sidebar to navigate:
    - **Prediction**: Enter customer details to get churn prediction.  
    - **Insights**: Explore churn-related trends.  
    - **About**: Learn more about the project.  
    """
    )
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=300)
