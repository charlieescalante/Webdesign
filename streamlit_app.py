import streamlit as st

# Page Config
st.set_page_config(
    page_title="PocketGuide 3.0",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS for Design
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #f9f9f9, #fff);
            font-family: 'Poppins', sans-serif;
            color: #2c3e50;
        }
        .banner {
            text-align: center;
            margin-bottom: 30px;
        }
        .banner img {
            width: 100%;
            max-height: 300px;
            object-fit: cover;
            border-radius: 10px;
        }
        .title {
            font-size: 50px;
            font-weight: 700;
            color: #34495e;
            margin: 20px 0;
        }
        .subtitle {
            font-size: 20px;
            color: #7f8c8d;
            margin-bottom: 40px;
        }
        .button-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 200px;
            gap: 20px;
        }
        .button {
            background-color: #ff6f61;
            color: white;
            font-size: 18px;
            padding: 15px 30px;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
        }
        .button:hover {
            background-color: #e74c3c;
            transform: scale(1.05);
        }
        .disclaimer {
            font-size: 14px;
            color: #95a5a6;
            text-align: center;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Banner Image
st.markdown("""
    <div class='banner'>
        <img src='https://i.imgur.com/IiVus2X.png' alt='Friendly Robot Tour Guide'>
    </div>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown("<div class='title'>PocketGuide 3.0</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your elegant travel companion, powered by AI.</div>", unsafe_allow_html=True)

# Buttons Logic
st.markdown("<div class='button-container'>", unsafe_allow_html=True)

if "stage" not in st.session_state:
    st.session_state.stage = 0

if st.session_state.stage == 0:
    if st.button("Fetch Coordinates", key="button1"):
        st.session_state.stage = 1

elif st.session_state.stage == 1:
    if st.button("Translate Address", key="button2"):
        st.session_state.stage = 2

elif st.session_state.stage == 2:
    if st.button("Start Tour", key="button3"):
        st.session_state.stage = 3

if st.session_state.stage == 3:
    st.success("Enjoy your journey! 🚀")

st.markdown("</div>", unsafe_allow_html=True)

# Disclaimer at the Bottom
st.markdown("<div class='disclaimer'>All information here is generated by an AI. Please verify all information to validate its truthfulness.</div>", unsafe_allow_html=True)
