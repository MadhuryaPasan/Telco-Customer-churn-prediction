import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# --- Data Loading and Model Setup (UNCHANGED) ---
# NOTE: File paths assume the script is run from a specific root directory structure.
try:
    before_preprocessing_dataset = pd.read_csv("Data Preprocessing/2.DataIntegration/02.integrated_telco_data.csv")
    data = pd.read_csv('Data Preprocessing/Model training/LogisticRegression/04.reduced_telco_data.csv')
except FileNotFoundError:
    st.error("Error: Dataset files not found. Please ensure 'integrated_telco_data.csv' and 'reduced_telco_data.csv' are in the correct relative paths.")
    st.stop()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Prepare data for model evaluation
y = data.iloc[:,6].values
tmp = data.drop(data.columns[6], axis=1)
X = tmp.iloc[:,:].values
X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size=0.8,
    random_state= 42,
    stratify=y,
)

# Load the trained model
model_filename = 'Data Preprocessing/Model training/LogisticRegression/logistic_regression_model.joblib'
try:
    loaded_model = joblib.load(model_filename)
except FileNotFoundError:
    st.error("Error: Model file 'logistic_regression_model.joblib' not found.")
    st.stop()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Make predictions on the test set
y_pred = loaded_model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
classification_report_result = classification_report(y_test, y_pred)

# --- Streamlit UI Function (Refactored) ---
def insights_page():
    
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
    
    st.set_page_config(layout="wide")
    
    st.markdown("<h1 style='text-align: center;'>Model Insights and Telco Dataset Analysis</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Section 1: Original Dataset Overview
    st.header("📋 Original Dataset (Before Preprocessing)")
    
    # Row 1: Dataset Preview and Key Stats
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("Dataset Preview (First 10 Rows)")
        st.dataframe(before_preprocessing_dataset.iloc[:10, 1:], use_container_width=True)
    
    with col2:
        st.subheader("Key Statistics")
        churn_rate = (before_preprocessing_dataset['Churn'].value_counts()['Yes'] / len(before_preprocessing_dataset)) * 100
        st.metric("Total Customers", len(before_preprocessing_dataset))
        st.metric("Churn Rate", f"{churn_rate:.1f}%")
        st.metric("Senior Citizens Count", f"{before_preprocessing_dataset['SeniorCitizen'].sum()}")
        st.markdown("**Note:** Features shown are non-encoded original values.Highly sensitive details are removed.")
    
    st.markdown("---") # Separator
    
    # Row 2: Charts for Original Data (Side-by-side)
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("1. Churn Distribution")
        fig1, ax1 = plt.subplots(figsize=(5, 4), dpi=80)
        churn_counts = before_preprocessing_dataset['Churn'].value_counts()
        ax1.pie(churn_counts.values, labels=churn_counts.index, autopct='%1.1f%%', startangle=90, colors=['#90EE90', '#FFA07A'])
        ax1.axis('equal')
        ax1.set_title('Overall Churn Distribution')
        plt.tight_layout()
        st.pyplot(fig1, use_container_width=False)  # Explicitly set to False
    
    with chart_col2:
        st.subheader("2. Churn by Gender")
        fig2, ax2 = plt.subplots(figsize=(5, 4), dpi=80)
        churn_by_gender = before_preprocessing_dataset.groupby(['gender', 'Churn']).size().unstack(fill_value=0)
        churn_by_gender.plot(kind='bar', ax=ax2, color=['skyblue', 'salmon'])
        ax2.set_title('Churn by Gender')
        ax2.set_ylabel('Count')
        ax2.tick_params(axis='x', rotation=0)
        ax2.legend(title='Churn')
        plt.tight_layout()
        st.pyplot(fig2, use_container_width=False)  # Explicitly set to False
    
    # Section 2: Processed Dataset Overview
    st.header("🔄 Processed Dataset (After Preprocessing & Reduction)")
    
    # Row 3: Processed Data Preview and Stats
    col3, col4 = st.columns([3, 2])
    with col3:
        st.subheader("Processed Data Preview (First 10 Rows)")
        st.dataframe(data.head(10), use_container_width=True)
    
    with col4:
        st.subheader("Processed Metrics")
        processed_churn_rate = (data.iloc[:, 6].value_counts().get(1, 0) / len(data)) * 100
        st.metric("Total Customers (Used)", len(data))
        st.metric("Churn Rate (Processed)", f"{processed_churn_rate:.1f}%")
        st.metric("Features Used", data.shape[1] - 1)
        st.markdown("**Note:** This is the cleaned, scaled, and encoded data fed to the model.")
    
    st.markdown("---") # Separator
    
    # Section 3: Model Performance
    st.header("🤖 Logistic Regression Model Performance")
    st.markdown("---")
    
    # Row 5: Accuracy and Confusion Matrix vs Classification Report (Side-by-side)
    col5, col6 = st.columns([1, 1])
    
    with col5:
        st.subheader("Model Evaluation & Confusion Matrix")
        st.metric("Test Accuracy", f"{accuracy:.2%}")
        cm = confusion_matrix(y_test, y_pred)
        fig5, ax5 = plt.subplots(figsize=(5, 4), dpi=80)
        sns.heatmap(cm, annot=True, fmt='d', cmap='mako', ax=ax5,
                    xticklabels=['No Churn (0)', 'Churn (1)'],
                    yticklabels=['No Churn (0)', 'Churn (1)'])
        ax5.set_title('Confusion Matrix')
        ax5.set_xlabel('Predicted')
        ax5.set_ylabel('Actual')
        plt.tight_layout()
        st.pyplot(fig5, use_container_width=False)  # Explicitly set to False
    
    with col6:
        st.subheader("Detailed Classification Report")
        st.code(classification_report_result, language='text')
    
    # Row 6: Feature Coefficients (Importance) - Full width for better readability
    st.subheader("📈 Feature Importance (Logistic Regression Coefficients)")
    
    # Prepare coefficient data
    coef_df = pd.DataFrame({
        'Feature': tmp.columns,
        'Coefficient': loaded_model.coef_[0]
    }).sort_values('Coefficient', key=abs, ascending=False)
    
    fig6, ax6 = plt.subplots(figsize=(8, 4), dpi=80)
    sns.barplot(data=coef_df.head(10), x='Coefficient', y='Feature', hue='Feature', ax=ax6, palette='rocket', legend=False)
    ax6.set_title('Top 10 Feature Coefficients (Absolute Value Sorted)')
    ax6.set_xlabel('Coefficient Value (Impact on Log-Odds)')
    ax6.set_ylabel('Feature Name')
    plt.tight_layout()
    st.pyplot(fig6, use_container_width=False)  # Explicitly set to False
    
    st.markdown("---")
    
    # Section 4: Key Insights
    st.header("💡 Key Insights")
    st.markdown("""
    - **Churn Patterns**: **Higher churn** is typically observed in month-to-month contracts and fiber optic users, indicating areas of service risk.
    - **Model Strengths**: The model achieves a decent overall accuracy but shows stronger performance in **predicting non-churn** (high True Negatives) than churn (True Positives).
    - **Preprocessing Impact**: The model was trained using three different techniques: Logistic Regression, MLP Classifier, and Decision Tree. The performance of these models was compared, and from this analysis, Logistic Regression was determined to be the best model.
    """)

        # Footer
    st.markdown(
        "<div class='footer'>"
        "Built with  by RuleQuest | Telco Customer Churn Prediction Project | "
        "Driving Customer Retention Through AI Innovation"
        "</div>",
        unsafe_allow_html=True,
    )