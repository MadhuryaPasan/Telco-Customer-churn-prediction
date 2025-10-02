

import streamlit as st
import base64

# Function to convert image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def home_page():
    # Load and convert local image
    image_path = "sub_pages/assets/telco_image.jpg"
    image_base64 = get_base64_of_image(image_path)

    # Inject CSS with base64 image
    page_bg = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    body {{
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #e0f7ff, #a1c4fd, #ffffff);
        color: #000000;
    }}

    .slideUp {{
        animation: slideUp 1s ease forwards;
        opacity: 0;
    }}
    .card1 {{ animation-delay: 0.2s; }}
    .card2 {{ animation-delay: 0.5s; }}
    .card3 {{ animation-delay: 0.8s; }}

    @keyframes slideUp {{
        from {{ transform: translateY(40px); opacity: 0; }}
        to {{ transform: translateY(0); opacity: 1; }}
    }}

    h1 {{
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #000000, #333333, #666666);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: slideUp 1s ease forwards;
        opacity: 0;
    }}

    .subtitle {{
        text-align: center;
        font-size: 1.3rem;
        font-weight: 400;
        color: #000000;
        margin-bottom: 2rem;
        animation: slideUp 1s ease forwards;
        animation-delay: 0.3s;
        opacity: 0;
    }}

    .welcome {{
        text-align: center;
        font-size: 1.8rem;
        font-weight: 600;
        color: #000000;
        margin: 2rem 0;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.25);
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    .description {{
        text-align: center;
        font-size: 1.2rem;
        line-height: 1.6;
        color: #000000;
        margin: 1.5rem 0;
        padding: 0 2rem;
    }}

    .highlight {{
        background: linear-gradient(120deg, #ffeb3b 0%, #ffeb3b 100%);
        background-repeat: no-repeat;
        background-size: 100% 0.3em;
        background-position: 0 88%;
        padding: 0.1rem 0.3rem;
        border-radius: 4px;
        font-weight: 600;
        color: #000000;
    }}

    .explore {{
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 3rem 0 2rem 0;
        color: #000000;
        position: relative;
        display: inline-block;
        left: 50%;
        transform: translateX(-50%);
        padding: 0 2rem;
    }}

    .explore::after {{
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #ff5722, #4caf50, #2196f3);
        border-radius: 2px;
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

    .card {{
        position: relative;
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 128, 0.1);
        overflow: hidden;
        opacity: 0;
        transition: all 0.4s ease;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}

    .card::before {{
        content: "";
        position: absolute;
        top: -60%;
        left: -60%;
        width: 220%;
        height: 220%;
        background: linear-gradient(120deg, rgba(255,255,255,0.4), transparent, rgba(255,255,255,0.15));
        transform: rotate(25deg);
        animation: shine 8s infinite linear;
        pointer-events: none;
    }}

    @keyframes shine {{
        0% {{ transform: rotate(25deg) translateX(-100%); }}
        100% {{ transform: rotate(25deg) translateX(100%); }}
    }}

    .card:hover {{
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 40px rgba(0, 0, 128, 0.2);
        background: rgba(255, 255, 255, 0.3);
    }}

    .card h4 {{
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #000000;
    }}

    .card p {{
        font-size: 1rem;
        line-height: 1.5;
        color: #000000;
        margin: 0;
    }}

    .divider {{
        height: 3px;
        background: linear-gradient(90deg, transparent, rgba(0, 0, 0, 0.3), transparent);
        margin: 2rem 0;
        border: none;
    }}

    /* Hero Section with Local Image */
    .hero-section {{
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                    url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        padding: 80px 20px;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
        color: white;
        position: relative;
        overflow: hidden;
    }}

    .hero-content {{
        position: relative;
        z-index: 2;
    }}

    .hero-title {{
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}

    .hero-subtitle {{
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }}

    .hero-description {{
        font-size: 1.2rem;
        line-height: 1.6;
        max-width: 800px;
        margin: 0 auto;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }}
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

    # Hero Section
    st.markdown(
        '''
        <div class="hero-section">
            <div class="hero-content">
                <div class="hero-title">Telco Customer Churn Prediction</div>
                <div class="hero-subtitle">Advanced AI-powered Customer Retention Solution</div>
                <div class="hero-description">
                    Use our intelligent AI system to identify customers at risk of churning and take 
                    proactive measures to enhance customer retention and drive business growth.
                </div>
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Explore Section
    st.markdown('<div class="explore">Explore the App</div>', unsafe_allow_html=True)

    # Feature Cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="card slideUp card1">'
            '<h4>🔮 Prediction</h4>'
            '<p>Enter customer details and get instant churn predictions with confidence scores and actionable insights.</p>'
            '</div>', unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="card slideUp card2">'
            '<h4>📊 Insights</h4>'
            '<p>Visualize customer churn trends, patterns, and uncover key influencing factors through interactive dashboards.</p>'
            '</div>', unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="card slideUp card3">'
            '<h4>ℹ️ About</h4>'
            '<p>Learn about the project methodology, data sources, implementation details, and team information.</p>'
            '</div>', unsafe_allow_html=True
        )

    st.markdown("---")

    # Footer
    st.markdown(
        "<div class='footer'>"
        "Built with  by our team | Telco Customer Churn Prediction Project | "
        "Driving Customer Retention Through AI Innovation"
        "</div>",
        unsafe_allow_html=True,
    )
