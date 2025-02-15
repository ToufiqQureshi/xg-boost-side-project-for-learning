import streamlit as st
import numpy as np
import joblib
import xgboost
# 🔥 Model Load Karo
model = joblib.load('xgboost_model.pkl')

# 🌟 Streamlit UI Setup
st.title("🔥 Agrarian Fire Prediction App")
st.write("Enter environmental conditions to predict fire risk.")

# 📌 Input Features
temperature = st.number_input("🌡 Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
wind_speed = st.number_input("🌬 Wind Speed (km/h)", min_value=0.0, max_value=150.0, step=0.1)
soil_moisture = st.number_input("🌿 Soil Moisture (%)", min_value=0.0, max_value=100.0, step=0.1)

# 🎯 Prediction Button
if st.button("🔮 Predict Fire Risk"):
    input_data = np.array([[temperature, humidity, wind_speed, soil_moisture]])
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("🔥 High Fire Risk! Take Precautions!")
    else:
        st.success("✅ No Fire Risk. Conditions are Safe!")
