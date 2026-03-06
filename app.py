# Import necessary libraries
import pickle
import streamlit as st
import pandas as pd

# -----------------------------
# Load Model
# -----------------------------
with open("Linear_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Load Encoder
# -----------------------------
with open("encoder.pkl", "rb") as file1:
    encoder = pickle.load(file1)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("cleaned_data.csv")

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("Bangalore House Price Prediction")
    st.image("https://thumbs.dreamstime.com/b/green-houses-community-model-abstract-real-estate-logo-vector-professional-architecture-company-design-115154734.jpg")
    st.write("Enter house details to predict the price.")

# -----------------------------
# Main Title
# -----------------------------
st.title("🏠 Bangalore House Price Prediction App")

st.write("Fill the details below to estimate the house price.")

# -----------------------------
# Input Fields
# -----------------------------

#input fields

#'location','bhk','total_sqft','bath','encoded_loc'
location = st.selectbox("Location: ",options=df["location"].unique())

bhk = st.selectbox("bhk: ",options=sorted(df["bhk"].unique()))

total_sqft = st.number_input("Total_sqft: ",min_value=300)

bath = st.selectbox("No. of Restrooms: ",options=sorted(df["bath"].unique()))

#encoded the new location
encoded_loc = encoder.transform([location])

#new data preparation
new_data = [[bhk,total_sqft,bath,encoded_loc[0]]]

#prediction
col1,col2 = st.columns([1,2])

if col2.button("Predict House Price"):
    pred = model.predict(new_data)[0]
    pred = round(pred*100000)
    st.subheader(f"Predicted Price : Rs. {pred}")