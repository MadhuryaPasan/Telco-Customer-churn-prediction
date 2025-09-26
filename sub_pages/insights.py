import streamlit as st 

def insights_page():
    st.title("📈 Customer Churn Insights")
    st.write("Explore churn-related patterns and visualizations.")

    st.info(
        "📊 Placeholder for charts (you can add churn rate, demographics, tenure distribution, etc.)"
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Churn by Contract Type")
        st.bar_chart({"Month-to-month": [200], "One year": [80], "Two year": [50]})
    with col2:
        st.subheader("Churn by Internet Service")
        st.bar_chart({"DSL": [120], "Fiber optic": [180], "No": [30]})