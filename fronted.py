import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Flower Species Prediction")

st.markdown("Enter Flower details below:")

# Input fields

Id = st.number_input("Id")

SepalLengthCm = st.number_input("SepalLengthCm")

SepalWidthCm = st.number_input("SepalWidthCm")

PetalLengthCm= st.number_input("PetalLengthCm")

PetalWidthCm = st.number_input("PetalWidthCm")

#TotalFloors = st.number_input("TotalFloors", min_value=1, value=70)

#location = st.text_input("location", value="Mumbai")

#State_California = st.number_input("State_California")
#State_NewYork = st.number_input("State_NewYork")

if st.button("Predict Flower Species"):
    input_data = {
        "Id" :Id,
        "SepalLengthCm" :SepalLengthCm,
        "SepalWidthCm" :SepalWidthCm,
        "PetalLengthCm" :PetalLengthCm,
        "PetalWidthCm" :PetalWidthCm,
        #"State_NewYork" :State_NewYork,
        #"location" :location,
        #"Furnishing" :Furnishing

    }

    response = requests.post(API_URL,json=input_data)
    if response.status_code==200:
        result = response.json()
        st.success(f'Predicted Flower Species :**{result['Predicted_category']}**')


