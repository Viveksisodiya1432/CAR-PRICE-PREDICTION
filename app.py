import streamlit as st
import pandas as pd
import scikit-learn
import joblib

# Page config
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# Load model
model = joblib.load("RandomForestRegressor.joblib")

# Title
st.markdown(
    "<h1 style='text-align: center; color:#2E86C1;'>Car Price Prediction </h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Enter car details to estimate the market price</p>",
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.header("Enter Car Details")

name = st.sidebar.text_input("Car Name", "BMW 3 Series")

company = st.sidebar.text_input("Company", "BMW")

year = st.sidebar.number_input(
    "Manufacturing Year",
    min_value=1995,
    max_value=2025,
    value=2020
)

kms_driven = st.sidebar.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=20000
)

fuel_type = st.sidebar.selectbox(
    "Fuel Type",
    ["Petrol","Diesel","CNG","LPG"]
)

st.write("")

# Predict button
if st.sidebar.button("Predict Price 💰"):

    input_data = pd.DataFrame({
        "name":[name],
        "company":[company],
        "year":[year],
        "kms_driven":[kms_driven],
        "fuel_type":[fuel_type]
    })

    prediction = model.predict(input_data)
    price = int(prediction[0])

    st.markdown("---")

    st.markdown(
        f"""
        <div style="background-color:#D5F5E3;
                    padding:30px;
                    border-radius:10px;
                    text-align:center;">
        <h2 style="color:#1E8449;">Estimated Car Price</h2>
        <h1 style="color:#1E8449;">₹ {price:,}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:grey;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
