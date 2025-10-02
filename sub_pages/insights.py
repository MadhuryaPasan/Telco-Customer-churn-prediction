import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model

def insights_page():
    # ----------------------------
    # Page Config
    # ----------------------------
    st.set_page_config(
        page_title="Customer Churn Insights",
        layout="wide",
    )

    # ----------------------------
    # CSS Styling (Dashboard Cards)
    # ----------------------------
    st.markdown("""
        <style>
        h1 { text-align: center; color: #222; margin-bottom: 20px; }
        .metric-card {
            background: #fff;
            border-radius: 14px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .metric-title { font-size: 15px; font-weight: 500; color: #444; margin-bottom: 8px; }
        .metric-value { font-size: 28px; font-weight: bold; color: #1d4ed8; margin-bottom: 6px; }
        .metric-change { font-size: 13px; font-weight: 500; }
        .up { color: green; }
        .down { color: red; }
        .chart-card {
            background: #fff;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # ----------------------------
    # Page Title
    # ----------------------------
    st.title("Customer Churn Insights")

    # ----------------------------
    # Load Dataset & Model
    # ----------------------------
    DATA_PATH = "Data Preprocessing/4.Data Reduction/04.reduced_telco_data.csv"
    MODEL_PATH = "helper/telco_churn_prediction_model_V1.0.keras"

    df = pd.read_csv(DATA_PATH)
    model = load_model(MODEL_PATH)

    target_col = "Churn"
    features = [col for col in df.columns if col != target_col]

    X = df[features]
    Y = df[target_col]
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.20, random_state=42, stratify=Y
    )

    # ----------------------------
    # Model Evaluation
    # ----------------------------
    results = model.evaluate(X_test, Y_test, verbose=0)
    
    loss = results[0]
    accuracy = results[1] if len(results) > 1 else None
    precision = results[2] if len(results) > 2 else None
    recall = results[3] if len(results) > 3 else None

    # Format values
    loss_val = f"{loss:.4f}"
    acc_val = f"{accuracy:.1%}" if accuracy is not None else "N/A"
    prec_val = f"{precision:.1%}" if precision is not None else "N/A"
    recall_val = f"{recall:.1%}" if recall is not None else "N/A"

    # Calculate churn rate
    churn_rate = df[target_col].mean()
    churn_val = f"{churn_rate:.1%}"

   
    # ----------------------------
    # Display Metrics
    # ----------------------------
    st.markdown("## Key Model Performance")
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Model Accuracy</div>
                <div class="metric-value">{acc_val}</div>
               
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Model Precision</div>
                <div class="metric-value">{prec_val}</div>
                
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Model Recall</div>
                <div class="metric-value">{recall_val}</div>
                
            </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Model Loss</div>
                <div class="metric-value">{loss_val}</div>
            </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Overall Churn Rate</div>
                <div class="metric-value">{churn_val}</div>
                
            </div>
        """, unsafe_allow_html=True)

    # ----------------------------
    # Data Visualizations
    # ----------------------------
    st.markdown("## Churn Patterns Analysis")
    colA, colB = st.columns(2)

    # Plot 1: Churn Distribution
    with colA:
        with st.container():
            st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
            fig, ax = plt.subplots(figsize=(5, 3))  # Smaller size
            sns.set_style("whitegrid")

            custom_palette = ["#4caf50", "#ff5722"]

            bar = sns.countplot(
                data=df, 
                x=target_col, 
                hue=target_col, 
                palette=custom_palette, 
                ax=ax,
                edgecolor="white",
                legend=False
            )
            ax.set_title("Churn Distribution", fontsize=12, fontweight="bold", pad=10)
            ax.set_xlabel("Churn Status", fontsize=10)
            ax.set_ylabel("Count", fontsize=10)
            ax.grid(axis="y", linestyle="--", alpha=0.7)
            sns.despine(left=True, bottom=True)
            st.pyplot(fig)
            st.markdown("</div>", unsafe_allow_html=True)

    # Plot 2: Churn Rate by Contract Type (using REAL data)
    with colB:
        with st.container():
            st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
            
            # Check if 'Contract' column exists in the dataset
            if 'Contract' in df.columns:
                # Calculate actual churn rates by contract type
                contract_churn = df.groupby('Contract')['Churn'].mean() * 100
                segments = contract_churn.index.tolist()
                churn_rates = contract_churn.values.tolist()
                
                # Sort by churn rate (highest to lowest) for better visualization
                sorted_data = sorted(zip(segments, churn_rates), key=lambda x: x[1], reverse=True)
                segments = [item[0] for item in sorted_data]
                churn_rates = [item[1] for item in sorted_data]
                
                chart_title = 'Churn Rate by Contract Type'
                xlabel = 'Contract Type'
                
            else:
                # Fallback: Check for other potential segment columns
                segment_columns = ['PaymentMethod', 'InternetService', 'SeniorCitizen']
                segment_found = False
                
                for col in segment_columns:
                    if col in df.columns:
                        segment_churn = df.groupby(col)['Churn'].mean() * 100
                        segments = segment_churn.index.tolist()
                        churn_rates = segment_churn.values.tolist()
                        
                        # Sort by churn rate
                        sorted_data = sorted(zip(segments, churn_rates), key=lambda x: x[1], reverse=True)
                        segments = [item[0] for item in sorted_data]
                        churn_rates = [item[1] for item in sorted_data]
                        
                        chart_title = f'Churn Rate by {col}'
                        xlabel = col
                        segment_found = True
                        break
                
                if not segment_found:
                    # Final fallback to sample data
                    segments = ['Month-to-month', 'One year', 'Two year']
                    churn_rates = [45.0, 12.0, 3.0]  # Typical telecom churn patterns
                    chart_title = 'Churn Rate by Contract Type (Sample)'
                    xlabel = 'Contract Type'
                    st.warning("⚠️ 'Contract' column not found - using sample data")
            
            # Create the bar chart with smaller size
            fig, ax = plt.subplots(figsize=(5, 3))
            
            # Use orange color for all bars
            colors = ['#2196f3'] * len(segments)
            
            # Create the bars
            bars = ax.bar(segments, churn_rates, color=colors, edgecolor='black', linewidth=0.5)
            
            # Customize the chart with smaller font sizes
            ax.set_title(chart_title, fontsize=12, fontweight='bold', pad=10)
            ax.set_ylabel('Churn Rate (%)', fontsize=10)
            ax.set_xlabel(xlabel, fontsize=10)
            
            # Rotate x-axis labels if they are long
            if any(len(str(segment)) > 10 for segment in segments):
                plt.xticks(rotation=45, ha='right')
            
            # Add value labels on top of each bar with smaller font
            for i, bar in enumerate(bars):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                        f'{height:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=9)
            
            # Set y-axis limit to give some space above the bars
            ax.set_ylim(0, max(churn_rates) + 5 if churn_rates else 35)
            
            # Customize grid and spines
            ax.grid(axis='y', linestyle='--', alpha=0.7)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
            
            # Adjust layout to prevent label cutoff
            plt.tight_layout()
            
            st.pyplot(fig)
            
           

# ----------------------------
if __name__ == "__main__":
    insights_page()