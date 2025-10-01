import streamlit as st


def insights_page():
    # st.title("📈 Customer Churn Insights")

    st.title("ℹ️ Input Fields Explanation")

    st.markdown(
        """
    Here’s an explanation of each input field used in the Telco Customer Churn Prediction form:

    ---

    ### 👤 Customer Information

    - **Gender**: The gender of the customer. Options are Male, Female, or Unknown.
    - **Senior Citizen**: Indicates if the customer is a senior citizen (Yes/No).
    - **Partner**: Whether the customer has a partner (Yes/No/Unknown).
    - **Dependents**: Whether the customer has dependents (Yes/No/Unknown).
    - **Tenure (months)**: The number of months the customer has been with the company.

    ---

    ### 📞 Phone & Internet Services

    - **Phone Service**: Whether the customer has a phone service (Yes/No).
    - **Multiple Lines**: Whether the customer has multiple phone lines (Yes/No/Unknown).
    - **Paperless Billing**: Whether the customer uses paperless billing (Yes/No).
    - **Internet Service**: Type of internet service the customer has: DSL, Fiber optic, or No Internet.
    - **Contract**: Type of contract the customer has: Month-to-Month, One year, or Two year.

    ---

    ### 💻 Additional Services

    - **Online Security**: Whether the customer has subscribed to online security service (Yes/No/Unknown).
    - **Online Backup**: Whether the customer uses online backup service (Yes/No/Unknown).
    - **Device Protection**: Whether the customer has device protection (Yes/No/Unknown).
    - **Tech Support**: Whether the customer has tech support subscription (Yes/No/Unknown).
    - **Streaming TV**: Whether the customer subscribes to streaming TV services (Yes/No/Unknown).
    - **Streaming Movies**: Whether the customer subscribes to streaming movies services (Yes/No/Unknown).

    ---

    ### 💳 Billing & Payment

    - **Payment Method**: The method the customer uses to pay bills: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic), or Unknown.
    - **Monthly Charges ($)**: The amount the customer is charged per month.
    - **Total Charges ($)**: The total amount the customer has been charged to date `(calculated as Monthly Charges × Tenure)`.

    ---
    """
    )

    # st.write("Explore churn-related patterns and visualizations.")

    # st.info(
    #     "📊 Placeholder for charts (you can add churn rate, demographics, tenure distribution, etc.)"
    # )

    # col1, col2 = st.columns(2)
    # with col1:
    #     st.subheader("Churn by Contract Type")
    #     st.bar_chart({"Month-to-month": [200], "One year": [80], "Two year": [50]})
    # with col2:
    #     st.subheader("Churn by Internet Service")
    #     st.bar_chart({"DSL": [120], "Fiber optic": [180], "No": [30]})
