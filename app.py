import streamlit as st
from sub_pages.prediction import prediction_page
from sub_pages.insights import insights_page
from sub_pages.about import about_page
from sub_pages.home import home_page

# --- Page Config ---
st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    # page_icon="📊",
    layout="wide",
)


# --- Sidebar ---
st.sidebar.title("⚙️ Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📋 Prediction", "📈 Insights", "ℹ️ About"])

# --- Home Page ---
if page == "🏠 Home":
    home_page()

# --- Prediction Page ---
elif page == "📋 Prediction":
    prediction_page()

# --- Insights Page ---
elif page == "📈 Insights":
    insights_page()


# --- About Page ---
elif page == "ℹ️ About":
    about_page()
