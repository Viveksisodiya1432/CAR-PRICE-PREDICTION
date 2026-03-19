import streamlit as st
import pandas as pd
import joblib

# Page Config
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# Load Model
model = joblib.load("RandomForestRegressor.joblib")

# Header
st.markdown("""
<style>
.big-title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#1F618D;
}
.subtitle {
    text-align:center;
    font-size:18px;
    color:grey;
}
.result-card {
    background: linear-gradient(135deg,#D4EFDF,#A9DFBF);
    padding:40px;
    border-radius:15px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🚗 Car Price Prediction Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter car details and estimate the market price instantly</p>', unsafe_allow_html=True)

st.markdown("---")

# Layout
col1, col2 = st.columns([1,2])

# Sidebar style inputs
with col1:

    st.subheader("🔧 Car Details")

    name = st.text_input("Car Name", "BMW 3 Series")

    company = st.text_input("Company", "BMW")

    year = st.slider(
        "Manufacturing Year",
        1995,
        2025,
        2020
    )

    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        max_value=500000,
        value=20000
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol","Diesel","CNG","LPG"]
    )

    predict = st.button("Predict Price 💰")

# Right side dashboard
with col2:

    st.subheader("📊 Prediction Result")

    if predict:

        input_data = pd.DataFrame({
            "name":[name],
            "company":[company],
            "year":[year],
            "kms_driven":[kms_driven],
            "fuel_type":[fuel_type]
        })

        try:

            prediction = model.predict(input_data)
            price = int(prediction[0])

            st.markdown(
                f"""
                <div class="result-card">
                <h2>Estimated Car Price</h2>
                <h1>₹ {price:,}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        except:
            st.error("⚠️ Prediction failed. Please check inputs.")

    else:
        st.info("Enter car details and click **Predict Price**")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:grey'>Made by Vivek | Powered by Streamlit 🚀</p>",
    unsafe_allow_html=True
)