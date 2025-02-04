import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set the page configuration
st.set_page_config(
    page_title="Prediction of Disease Outbreak",
    layout="wide",
    page_icon="doctor.png"
)

# Load the diabetes model
diabetes_model = pickle.load(open(r"D:\vishnu\disease outbreak\training_model\Saved_models\diabetes_model.sav", "rb"))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Prediction of Disease Outbreak System",
        ["Diabetes", "Heart Disease", "Parkinson's Disease"],
        menu_icon="Hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0
    )

# Diabetes Prediction
if selected == "Diabetes":
    st.title("Diabetes Prediction System Using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        glucose = st.text_input("Glucose Level")
    with col3:
        blood_pressure = st.text_input("Blood Pressure")
    with col1:
        skin_thickness = st.text_input("Skin Thickness")
    with col2:
        insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function")
    with col2:
        age = st.text_input("Age of the Person")

   
diab_diagnosis =" "
if st.button("Diabetes Prediction"):
    user_input=[pregnancies,glucose,blood_pressure,skin_thickness,insulin,BMI,diabetes_pedigree_function,age]
    user_input=[float(x) for x in user_input]
    diab_prediction=diabetes_model.predict([user_input])
    if diab_prediction[0]==1:
        diab_diagnosis="The person is diabetic"
    else:
        diab_diagnosis="The person is not diabetic"
st.success(diab_diagnosis)