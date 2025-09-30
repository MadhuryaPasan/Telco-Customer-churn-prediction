import streamlit as st

def home_page():
    page_bg = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(135deg, #e0f7ff, #a1c4fd, #ffffff);
        color: #1a237e;
    }

    .slideUp {
        animation: slideUp 1s ease forwards;
        opacity: 0;
    }
    .card1 { animation-delay: 0.2s; }
    .card2 { animation-delay: 0.5s; }
    .card3 { animation-delay: 0.8s; }

    @keyframes slideUp {
        from { transform: translateY(40px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    h1 {
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        color: #0d47a1;
        animation: slideUp 1s ease forwards;
        opacity: 0;
    }

    .welcome {
        text-align: center;
        font-size: 24px;
        font-weight: 700;
        color: #1565c0;
    }

    .description {
        text-align: center;
        font-size: 18px;
       
    }

    .explore {
        text-align: center;
        font-size: 30px;
        font-weight: 800;
        margin: 30px 0 20px 0;
       
    }

    .footer {
        text-align: center;
        color: #555;
        font-size: 15px;
        margin-top: 25px;
    }

    .card {
        position: relative;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 4px 12px rgba(0, 0, 128, 0.1); /* softer shadow */
        overflow: hidden;
        opacity: 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
    }

    .card::before {
        content: "";
        position: absolute;
        top: -60%;
        left: -60%;
        width: 220%;
        height: 220%;
        background: linear-gradient(120deg, rgba(255,255,255,0.35), transparent, rgba(255,255,255,0.1));
        transform: rotate(25deg);
        animation: shine 6s infinite linear;
        pointer-events: none;
    }

    @keyframes shine {
        0% { transform: rotate(25deg) translateX(-100%); }
        100% { transform: rotate(25deg) translateX(100%); }
    }

    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 8px 24px rgba(0, 0, 128, 0.15); /* softer hover */
    }

    /* Card Titles - Different Colors */
    .card1 h4 { color: #ff5722; } /* Orange */
    .card2 h4 { color: #4caf50; } /* Green */
    .card3 h4 { color: #2196f3; } /* Blue */

    .card p {
        font-size: 16px;
        margin-top: 8px;
        color: #0d47a1;
    }

    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)


    st.markdown('<h1>Telco Customer Churn Prediction</h1>', unsafe_allow_html=True)
    st.markdown("---")


    st.markdown(
        '<div class="welcome">'
        'Welcome to the Customer Churn Prediction System</div>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

  
    st.markdown(
        '<div class="description">'
        'Use this tool to identify <b>customers at risk of churning</b> based on demographics, services, and billing information.'
        '</div>',
        unsafe_allow_html=True,
    )


    st.markdown('<div class="explore">Explore the App</div>', unsafe_allow_html=True)

 
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="card slideUp card1">'
            '<h4>Prediction</h4>'
            '<p>Enter customer details and get instant churn predictions with confidence score.</p>'
            '</div>', unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            '<div class="card slideUp card2">'
            '<h4>Insights</h4>'
            '<p>Visualize customer churn trends and uncover key influencing factors.</p>'
            '</div>', unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            '<div class="card slideUp card3">'
            '<h4>About</h4>'
            '<p>Learn about the project, data sources, and implementation details.</p>'
            '</div>', unsafe_allow_html=True
        )

    st.markdown("---")

    
    st.markdown(
        "<div class='footer'>Built with  by our team | Telco Customer Churn Prediction Project</div>",
        unsafe_allow_html=True,
    )
