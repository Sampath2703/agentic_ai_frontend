import streamlit as st
import requests


backend_url = st.secrets["backend_url"]

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1441974231531-c6227db76b6e");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    h1 {
        color: white !important;
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
    
    data = res.json()["msg"]

    if res.status_code == 200:
        with st.form():


            st.warning(f"City: {data['city']}")
            st.warning(f"Temperature: {data['temp']}°C")
            st.warning(f"Humidity: {data['humidity']}%")
            st.warning(f"Wind Speed: {data['wind_speed']} m/s")

            st.warning(data["answer"])
