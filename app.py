import streamlit as st
import requests


backend_url = st.secrets["backend_url"]

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1470770841072-f978cf4d019e");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    h1 {
        color: brown !important;
        text-align: center;
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 30px;
    }

    /* Custom style for your side headings */
    .custom-label {
        font-size: 38px; /* Adjust this number to make it as big as you want */
        font-weight: 800;
        color: black;
        margin-bottom: -35px; /* Pulls the heading closer to its text box */
    }

    .block-container {
        padding-top: 12rem;
    }

    .stTextInput > div > div > input {
        height: 45px;
        font-size: 16px;
        color: white !important;
        background-color: rgba(0,0,0,0.3);
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title
st.markdown("<h1>🌦️ AI Weather Forecast</h1>", unsafe_allow_html=True)

# City Section
st.markdown('<p class="custom-label">City</p>', unsafe_allow_html=True)
city = st.text_input("", key="city_input")

# State Section
st.markdown('<p class="custom-label">Question</p>', unsafe_allow_html=True)
question = st.text_input("", key="question_input")


button = st.button("Get Weather")

if button:
    res = requests.post(
    f"{backend_url}/get_weather",
    json={
        "city": city,
        "question": question
    }
    )


    st.write("Status:", res.status_code)
    st.write("Raw Response:")
    st.code(res.text)

    if res.status_code == 200:
        data = res.json()["msg"]