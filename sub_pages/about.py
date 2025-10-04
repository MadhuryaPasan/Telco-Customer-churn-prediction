import streamlit as st


def about_page():
    page_bg = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .hero-section {{
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.95), rgba(118, 75, 162, 0.95));
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }}
    
    .hero-title {{
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }}
    
    .hero-subtitle {{
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.9);
        font-weight: 400;
    }}

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

    st.markdown(
        """
    <div class='hero-section'>
        <div class='hero-title'>About This App</div>
        <div class='hero-subtitle'>Intelligent customer churn prediction system for telecommunications companies</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📋 Overview")
    st.markdown(
        """
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #4CAF50;">
    The <b>Telco Customer Churn Prediction System</b> is an intelligent analytics platform 
    designed to revolutionize customer retention strategies in the telecommunications industry. 
    By harnessing the power of machine learning and real-time data analytics, we empower 
    businesses to proactively identify at-risk customers and implement effective retention measures.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### 🚀 Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 15px; height: 200px;">
        <h4 style="color: white;">🔮 Smart Predictions</h4>
        <p>Advanced ML algorithms deliver real-time churn predictions with confidence scoring and risk assessment</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 20px; border-radius: 15px; height: 200px;">
        <h4 style="color: white;">📊 Deep Insights</h4>
        <p>Interactive dashboards reveal churn patterns, customer behavior trends, and key influencing factors</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 20px; border-radius: 15px; height: 200px;">
        <h4 style="color: white;">🎯 Actionable Intelligence</h4>
        <p>Customer segmentation and personalized retention strategies based on predictive analytics</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    st.markdown("### 💼 Business Impact")

    impact_col1, impact_col2 = st.columns(2)

    with impact_col1:
        st.markdown(
            """
        <div style="background-color: #e3f2fd; padding: 15px; border-radius: 10px; margin-bottom: 15px;">
        <h4 style="color: #1565c0;">📈 Revenue Protection</h4>
        <ul>
        <li>Prevent revenue loss from customer attrition</li>
        <li>Increase customer lifetime value</li>
        <li>Optimize resource allocation for retention</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div style="background-color: #fff3e0; padding: 15px; border-radius: 10px;">
        <h4 style="color: #ef6c00;">⚡ Operational Excellence</h4>
        <ul>
        <li>Automated risk scoring for entire customer base</li>
        <li>Real-time prediction capabilities</li>
        <li>Scalable solution for growing data needs</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with impact_col2:
        st.markdown(
            """
        <div style="background-color: #fce4ec; padding: 15px; border-radius: 10px; margin-bottom: 15px;">
        <h4 style="color: #c2185b;">🎯 Strategic Advantage</h4>
        <ul>
        <li>Data-driven decision making</li>
        <li>Proactive customer relationship management</li>
        <li>Competitive edge in market retention</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div style="background-color: #e8f5e8; padding: 15px; border-radius: 10px;">
        <h4 style="color: #2e7d32;">🔍 Customer Insights</h4>
        <ul>
        <li>Understand customer behavior patterns</li>
        <li>Identify key churn drivers</li>
        <li>Personalize customer experiences</li>
        </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    # Footer
    st.markdown(
        "<div class='footer'>"
        "Built with  by RuleQuest | Telco Customer Churn Prediction Project | "
        "Driving Customer Retention Through AI Innovation"
        "</div>",
        unsafe_allow_html=True,
    )
