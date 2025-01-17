import streamlit as st
import numpy as np
import pickle

dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocesser = pickle.load(open('preprocesser.pkl','rb'))

def prediction(Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item):
    features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
    transform_features = preprocesser.transform(features)  # Transform the features using the preprocessor
    predicted_yield = dtr.predict(transform_features)  # Predict using the transformed features
    return predicted_yield[0]  # Return the single predicted value

st.title("Crop Yield Prediction")

Year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
average_rain_fall_mm_per_year = st.number_input("Average Rainfall (mm per year)")
pesticides_tonnes = st.number_input("Pesticides (Tonnes)")
avg_temp = st.number_input("Average Temperature (°C)")
Area = st.text_input("Area")  # You can map area names to a number or encode as needed
Item = st.text_input("Crop Item (e.g., 'Maize')")  # Encode the crop item as needed


if st.button("Predict"):
    # Make prediction
    result = prediction(Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item)
    st.write(f"Predicted Yield: {result} tons")