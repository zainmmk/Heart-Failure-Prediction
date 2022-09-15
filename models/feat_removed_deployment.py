import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
model = pickle.load(open('feat_imp_final_pipeline','rb'))
def predict_prob(Age,ChestPainType,RestingBP,Cholesterol,MaxHR,ExerciseAngina,Oldpeak,
                ST_Slope):
    input= {'Age':[Age],'ChestPainType':[ChestPainType],'RestingBP':[RestingBP],'Cholesterol':[Cholesterol],'MaxHR':[MaxHR],'ExerciseAngina':[ExerciseAngina],'Oldpeak':[Oldpeak],'ST_Slope':[ST_Slope]}
    input_df = pd.DataFrame.from_dict(input)
    prediction = model.predict_proba(input_df)
    
    return (prediction)
st.title("Heart disease probability prediction")
st.markdown("Using a number of features, this model will predict what it believes your probability of having heart disease is!")
Age = st.text_input("Age")
ChestPainType = st.selectbox("Chest Pain", ["SYM", "ASY"])
RestingBP = st.text_input("Resting Blood Pressure")
Cholesterol = st.text_input("Cholesterol")
MaxHR = st.text_input("Max Heart Rate")
ExerciseAngina = st.selectbox("Exercise Angina", ["Y","N"])
Oldpeak = st.text_input("Old Peak Measurement")
ST_Slope = st.selectbox("ST Slope",["Up","Down","Flat"])
if st.button("Predict probability"):
    output = predict_prob(Age,ChestPainType,RestingBP,Cholesterol,MaxHR,ExerciseAngina,Oldpeak,ST_Slope)
    st.success('The probability is {}%'.format(output[0][1]*100))
image = Image.open('../figures/HEART_INFO_treatments.png')
st.image(image, caption='Heart disease treatments/preventative measures')