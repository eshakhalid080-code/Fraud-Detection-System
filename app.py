import pandas as pd
import streamlit as st
import joblib

model = joblib.load("Fraud_detection_System.pkl")

st.title("Fraud Detection System /App🕵️")

st.markdown("Please enter Transaction Details and Click on Button ")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "CASH_OUT", "TRANSFER", "CASH_IN"])

amount= st.number_input("Amount 💰:", min_value=0.0, max_value=100000.0)

oldbalanceOrg= st.number_input("Old Balance (Sender):", min_value=0.0, max_value=100000.0)
newbalanceOrig= st.number_input("New Balance (Sender):", min_value=0.0, max_value=100000.0)

oldbalanceDest= st.number_input("Old Balance (Receiver):", min_value=0.0, max_value=100000.0)
newbalanceDest= st.number_input("New Balance (Receiver):", min_value=0.0, max_value=100000.0)

if st.button("Predict"):
    input_data= pd.DataFrame([{
        "type": transaction_type,
        "amount" : amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}' " ,divider="gray")

    if prediction==1:
        st.error("This Transaction can be a Fraud⚠️⚠️")
    else: 
        st.success("Safe Transaction")