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
diabetes_model = pickle.load(open(r"D:\vishnu\disease outbreak\Saved_models\diabetes_model.sav", "rb"))
Heart_model=pickle.load(open(r"D:\vishnu\disease outbreak\Saved_models\Heart_model.sav","rb"))
pakinsons_model=pickle.load(open(r"D:\vishnu\disease outbreak\Saved_models\pakinsons_model.sav","rb"))

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
        Pregnancies = st.text_input("Number of Pregnancies")
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
        user_input=[Pregnancies,glucose,blood_pressure,skin_thickness,insulin,BMI,diabetes_pedigree_function,age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis="The person is diabetic"
        else:
            diab_diagnosis="The person is not diabetic"
    st.success(diab_diagnosis)

#Heart Disease Prediction
if selected == "Heart Disease":
    st.title("Heart Disease Prediction System Using ML")
    col1, col2,col3 =st.columns(3)
    with col1:
        age =st.text_input("Age")
    with col2:
        sex=st.text_input("sex")
    with col3:
        cp=st.text_input("cp")
    with col1:
        trestbps=st.text_input("trestbps")
    with col2:
        chol=st.text_input("chol")
    with col3:
        fbs=st.text_input("fbs")
    with col1:
        restecg=st.text_input("restecg")
    with col2:
        thalach=st.text_input("thalach")
    with col3:
        exang=st.text_input("exang")
    with col1:
        oldpeak=st.text_input("oldpeak")
    with col2:
        slope=st.text_input("slope")
    with col3:
        ca=st.text_input("ca")
    with col1:
        thal=st.text_input("thal")
    
    heart_diagnosis =" "
    if st.button("Heart Disease Prediction"):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_prediction=Heart_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis = "The person is having heart disease"
        else:
                heart_diagnosis = "The person does not have heart disease"
    st.success(heart_diagnosis)




#Pakinsons_model
if selected=="Parkinson's Disease":
    st.title("Parkinson's Disease Prediction Using ML")
    col1,col2,col3=st.columns(3)
    with col1 :
        MDVP=st.text_input("Mean fundamental frequency (Fo) in Hertz")
    with col2:
        mdvp2=st.text_input(" Maximum fundamental frequency (Fhi) in Hertz")
    with col3:
        MDVP3=st.text_input("Minimum fundamental frequency (Flo) in Hertz")
    with col1:
        MDVP4=st.text_input("Percentage of Jitter (variation in fundamental frequency)")
    with col2:
        MDVP5=st.text_input("Absolute Jitter")
    with col3:
        MDVP6=st.text_input("Relative Average Perturbation (a measure of frequency perturbation)")
    with col1:
        MDVP7=st.text_input("Pitch Period Perturbation Quotient")
    with col2:
        jitter=st.text_input("Difference of Differences of Pitch")
    with col3:
        MDVP8=st.text_input(" Shimmer (variation in amplitude)")
    with col1:
        MDVP9=st.text_input("Shimmer in decibels")
    with col2:
        Shimme1=st.text_input("Three-point Amplitude Perturbation Quotient")
    with col3:
        Shimme2=st.text_input(" Five-point Amplitude Perturbation Quotient")
    with col1:
        MDVP10=st.text_input("Amplitude Perturbation Quotient")
    with col2:
        Shimme3=st.text_input("Degree of Amplitude Perturbation")
    with col3:
        NHR=st.text_input("Noise-to-Harmonics Ratio (measure of noise in voice)")
    with col1:
        HNR=st.text_input("Harmonics-to-Noise Ratio (HNR) (measure of noise in voice)")
    with col2:
        RPDE=st.text_input("Recurrence Period Density Entropy (nonlinear dynamical complexity measure)")
    with col3:
        DFA=st.text_input("Detrended Fluctuation Analysis (measures fractal scaling of signal)")
    with col1:
        spread1=st.text_input("Fundamental frequency variation (spread 1)")
    with col2:
        spread2=st.text_input(" Fundamental frequency variation (spread 2)")
    with col3:
        D2=st.text_input(" Correlation Dimension (measures signal complexity)")
    with col1:
        PPE=st.text_input("Pitch Period Entropy (represents randomness in pitch)")
    park_disease=" "
    if st.button("Parkinson's Disease Prediction Using ML"):
        user_input=[MDVP,mdvp2,MDVP3,MDVP4,MDVP5,MDVP6,MDVP7,jitter,MDVP8,MDVP9,Shimme1,Shimme2,MDVP10,Shimme3,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        park_prediciton=pakinsons_model.predict([user_input])
        if park_prediciton[0]==1:
            park_disease="The person is having Parkinson's disease"
        else:
            park_disease="The person does not having Parkinson's disease"            
    st.success(park_disease)          