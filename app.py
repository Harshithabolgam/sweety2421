import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('linear_model.joblib')  

# Sample input data (replace with your input)
# Assume your model expects a DataFrame as input
sample_input = pd.DataFrame({
    'MedInc': [1],
    'HouseAge': [2],
    'AveRooms': [3],
    'AveBedrms': [4],
    'Population': [5],
    'AveOccup': [6],
    'Latitude': [7],
    'Longitude': [8],
})

# Function to make predictions
def make_prediction(house_price_data):
    prediction = model.predict(house_price_data)[0]
    return prediction

# Streamlit UI
st.title("House Price Prediction")

# Example Input fields (adjust to your model's input)
MedInc = st.number_input("MedInc:", min_value=0, max_value=20)
HouseAge = st.number_input("HouseAge:", min_value=0, max_value=60)
AveRooms = st.number_input("AveRooms:", min_value=0, max_value=150)
AveBedrms = st.number_input("AveBedrms:", min_value=0, max_value=35)
Population = st.number_input("Population:", min_value=3, max_value=40000)
AveOccup = st.number_input("AveOccup:", min_value=0, max_value=1300)
Latitude = st.number_input("Latitude:", min_value=-125, max_value=125)
Longitude = st.number_input("Longitude:", min_value=0, max_value=6)

# Create input data for the model
new_input = pd.DataFrame({
    'feature1': [MedInc],
    'feature2': [HouseAge],
    'feature3': [AveRooms],
    'feature4': [AveBedrms],
    'feature5': [Population],
    'feature6': [AveOccup],
    'feature7': [Latitude],
    'feature8': [Longitude],

    # ... add other features from your UI
})

# Make a prediction
if st.button("Predict"):
    predicted_price = make_prediction(new_input)
    st.write(f"Predicted house price: ${predicted_price:.2f}")