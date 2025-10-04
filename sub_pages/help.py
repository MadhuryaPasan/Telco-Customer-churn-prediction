import streamlit as st


def help_page():
    # Custom CSS for improved UI
    page_bg = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .hero-section {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.95), rgba(118, 75, 162, 0.95));
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.9);
        font-weight: 400;
    }
    
    .info-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }
    
    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    .card-icon {
        font-size: 2rem;
        margin-right: 1rem;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .card-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin: 0;
    }
    
    .field-item {
        padding: 1rem;
        margin-bottom: 1rem;
        background: #f8f9fa;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        transition: all 0.2s ease;
    }
    
    .field-item:hover {
        background: #e9ecef;
        border-left-color: #764ba2;
    }
    
    .field-name {
        font-weight: 600;
        color: #667eea;
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
    }
    
    .field-description {
        color: #4a5568;
        line-height: 1.6;
        margin: 0;
    }
    
    .quick-tip {
        background: linear-gradient(135deg, #ffeaa7, #fdcb6e);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 2rem 0;
        border-left: 5px solid #f39c12;
    }
    
    .quick-tip-title {
        font-weight: 600;
        color: #2c3e50;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .footer {
        text-align: center;
        color: white;
        font-size: 0.95rem;
        margin-top: 3rem;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .footer strong {
        color: #ffd700;
    }
    
    /* Streamlit specific overrides */
    .stMarkdown {
        color: inherit;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

    # Hero Section
    st.markdown(
        """
    <div class='hero-section'>
        <div class='hero-title'> Field Guide & Help Center</div>
        <div class='hero-subtitle'>Understanding every input for accurate churn predictions</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quick Tip
    st.markdown(
        """
    <div class='quick-tip'>
        <div class='quick-tip-title'>💡 Quick Tip</div>
        <p style='margin: 0; color: #2c3e50;'>Fill out all fields accurately for the best prediction results. If you're unsure about a field, select "Unknown" where available.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Customer Information Card
    st.markdown(
        """
    <div class='info-card'>
        <div class='card-header'>
            <div class='card-icon'>👤</div>
            <h2 class='card-title'>Customer Information</h2>
        </div>
        <div class='field-item'>
            <div class='field-name'>Gender</div>
            <div class='field-description'>Select the customer's gender: Male, Female, or Unknown if not specified.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Senior Citizen</div>
            <div class='field-description'>Indicate whether the customer is 65 years or older.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Partner</div>
            <div class='field-description'>Does the customer have a spouse or partner? Select Yes, No, or Unknown.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Dependents</div>
            <div class='field-description'>Does the customer have dependents (children, parents, etc.)? Select Yes, No, or Unknown.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Tenure (months)</div>
            <div class='field-description'>Total number of months the customer has been with the company. Enter a value between 0-72 months.</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Phone & Internet Services Card
    st.markdown(
        """
    <div class='info-card'>
        <div class='card-header'>
            <div class='card-icon'>📞</div>
            <h2 class='card-title'>Phone & Internet Services</h2>
        </div>
        <div class='field-item'>
            <div class='field-name'>Phone Service</div>
            <div class='field-description'>Does the customer subscribe to phone services?</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Multiple Lines</div>
            <div class='field-description'>If phone service is active, does the customer have multiple phone lines?</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Internet Service</div>
            <div class='field-description'>Type of internet connection: DSL (slower), Fiber optic (faster), or No Internet service.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Contract Type</div>
            <div class='field-description'>Customer's contract duration: Month-to-Month (flexible), One year, or Two year (most commitment).</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Paperless Billing</div>
            <div class='field-description'>Does the customer receive bills electronically instead of paper mail?</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Additional Services Card
    st.markdown(
        """
    <div class='info-card'>
        <div class='card-header'>
            <div class='card-icon'>💻</div>
            <h2 class='card-title'>Additional Services</h2>
        </div>
        <div class='field-item'>
            <div class='field-name'>Online Security</div>
            <div class='field-description'>Protection against online threats and viruses. Available only with internet service.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Online Backup</div>
            <div class='field-description'>Cloud backup service for customer data. Available only with internet service.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Device Protection</div>
            <div class='field-description'>Insurance/protection plan for customer devices. Available only with internet service.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Tech Support</div>
            <div class='field-description'>24/7 technical assistance and troubleshooting service. Available only with internet service.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Streaming TV</div>
            <div class='field-description'>Television streaming service subscription. Available only with internet service.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Streaming Movies</div>
            <div class='field-description'>Movie streaming service subscription. Available only with internet service.</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Billing & Payment Card
    st.markdown(
        """
    <div class='info-card'>
        <div class='card-header'>
            <div class='card-icon'>💳</div>
            <h2 class='card-title'>Billing & Payment</h2>
        </div>
        <div class='field-item'>
            <div class='field-name'>Payment Method</div>
            <div class='field-description'>How the customer pays their bills: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic), or Unknown.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Monthly Charges ($)</div>
            <div class='field-description'>The customer's recurring monthly bill amount.</div>
        </div>
        <div class='field-item'>
            <div class='field-name'>Total Charges ($)</div>
            <div class='field-description'>Cumulative amount billed to date. Automatically calculated as Monthly Charges × Tenure.</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Footer
    st.markdown(
        "<div class='footer'>"
        "Built with  by RuleQuest | Telco Customer Churn Prediction Project | "
        "Driving Customer Retention Through AI Innovation"
        "</div>",
        unsafe_allow_html=True,
    )
