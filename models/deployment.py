import numpy as np
import pandas as pd
import streamlit as st
import pickle
model = pickle.load(open('final_pipeline','rb'))
def predict_prob(Sex,ChestPainType,FastingBS,ExerciseAngina,Oldpeak,
                ST_Slope):
    input= {'Sex':[Sex],'ChestPainType':[ChestPainType],'FastingBS':[FastingBS],'ExerciseAngina':[ExerciseAngina],'Oldpeak':[Oldpeak],'ST_Slope':[ST_Slope]}
    input_df = pd.DataFrame.from_dict(input)
    prediction = model.predict_proba(input_df)
    
    return (prediction)
st.title("Heart disease probability prediction")
st.markdown("Using a number of features, this model will predict what it believes your probability of having heart disease is!")
Sex = st.selectbox("Sex", ["M","F"])
ChestPainType = st.selectbox("Chest Pain", ["SYM", "ASY"])
FastingBS = st.selectbox("Blood sugar (> 120 mg/dl = 1, else 0)",[1,0])
ExerciseAngina = st.selectbox("Exercise Angina", ["Y","N"])
Oldpeak = st.text_input("Old Peak Measurement")
ST_Slope = st.selectbox("ST Slope",["Up","Down","Flat"])
if st.button("Predict probability!"):
    output = predict_prob(Sex,ChestPainType,FastingBS,ExerciseAngina,Oldpeak,ST_Slope)
    st.success('The probability is {}%'.format(output[0][1]*100))