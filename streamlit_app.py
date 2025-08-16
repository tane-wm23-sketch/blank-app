import streamlit as st
from joblib import load
import numpy as np

# Load the model
model = load('linear_regression_model.joblib')

# Create a simple user input
user_input = st.number_input('Enter house size:', min_value=100, max_value=10000, step=50)
user_input_2 = st.number_input('Enter num_bedrooms:', min_value=1, max_value=10, step=1)

# Combine inputs into a single 2D array [[house_size, num_bedrooms]]
input_array = np.array([[user_input, user_input_2]])

# Predict the house price
if st.button('Predict Price'):
    predicted_price = model.predict(input_array)
    st.write(f"The predicted house price is: ${predicted_price[0]:.2f}")
