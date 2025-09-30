import streamlit as st
from sub_pages.prediction import prediction_page
from sub_pages.insights import insights_page
from sub_pages.about import about_page
from sub_pages.home import home_page


st.set_page_config(
    page_title="Telco Customer Churn Prediction",
    layout="wide",
)


pages = {
    "Home": home_page,
    "Prediction": prediction_page,
    "Insights": insights_page,
    "About": about_page
}


if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


st.sidebar.title("Navigation")


st.markdown("""
    <style>
    div.stButton > button {
        all: unset;
        width: 180px;
        padding: 12px 20px;
        margin-bottom: 6px;
        border-radius: 8px;
        text-align: left;  /* left-aligned text */
        font-size: 16px;
        cursor: pointer;
        color: white;
        background-color: #2c3e50;
        font-weight: 500;
        transition: background-color 0.2s;
        display: block;
    }
    div.stButton > button:hover {
        background-color: #34495e;
    }
    div.stButton > button.active {
        background-color: #e67e22 !important;
        color: white !important;
        font-weight: bold;
        text-align: left;
        padding: 12px 20px;
    }
    </style>
""", unsafe_allow_html=True)


for page_name in pages.keys():
   
    is_active = page_name == st.session_state.current_page

   
    if st.sidebar.button(page_name, key=page_name, width='stretch'):
        st.session_state.current_page = page_name
        is_active = True  

    if is_active:
        st.markdown(f"""
        <style>
        div.stButton > button[key="{page_name}"] {{
            background-color: #e67e22 !important;
            font-weight: bold;
        }}
        </style>
        """, unsafe_allow_html=True)


pages[st.session_state.current_page]()
