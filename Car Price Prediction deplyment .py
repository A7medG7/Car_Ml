import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained models and inputs
best_model= joblib.load( 'best_model.pkl')
Inputs= joblib.load('Inputs.pkl')
Brand = joblib.load('Brand.pkl')
Model = joblib.load('Model.pkl')
Body = joblib.load('Body.pkl')
Color = joblib.load('Color.pkl')

Fuel = joblib.load('Fuel.pkl')
Kilometers = joblib.load('Kilometers.pkl')
Engine = joblib.load('Engine.pkl')
Transmission = joblib.load('Transmission.pkl')
Gov = joblib.load('Gov.pkl')
Car_age = joblib.load('Car_age.pkl')

st.title("Used Car Price Prediction App")
st.info("Easy App for Guess the car price")

Brand_inputs = st.selectbox('Brand ' , Brand )

Model_inputs = st.selectbox('Model ' , Model )
Body_inputs = st.selectbox('Body ' , Body )
Color_inputs = st.selectbox('Color ' , Color )
Fuel_inputs = st.selectbox('Fuel ' , Fuel )
Kilometers_inputs = st.selectbox('Kilometers ' , Kilometers )
Engine_inputs = st.selectbox('Engine ' , Engine )
Transmission_inputs = st.selectbox('Transmission ' , Transmission )
Gov_inputs = st.selectbox('Gov ' , Gov )
Car_age_inputs = st.selectbox('Car_age ' , Car_age )

# Welcome message in the sidebar
st.sidebar.header('Welcome to the Car Price Predictor!')
st.sidebar.write('Enter your car details and click the button to check the price.')

# Button to check the price
if st.sidebar.button('Check Price'):
    # Create a DataFrame with user inputs
    user_inputs = pd.DataFrame({
        'Brand': [Brand_inputs],
        'Model': [Model_inputs],
        'Body': [Body_inputs],
        'Color': [Color_inputs],
        'Fuel': [Fuel_inputs],
        'Kilometers': [Kilometers_inputs],
        'Engine': [Engine_inputs],
        'Transmission': [Transmission_inputs],
        'Gov': [Gov_inputs],
        'Car_age': [Car_age_inputs]
    })

    # Display the user inputs
    st.write('User Inputs:')
    st.write(user_inputs)

    # Now, you can pass the user_inputs DataFrame to your best model for prediction
    # Replace the following line with your actual prediction code
    predicted_price = best_model.predict(user_inputs)
    st.write('Predicted Price:', predicted_price)

