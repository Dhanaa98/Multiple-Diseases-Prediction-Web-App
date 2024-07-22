import pickle
import streamlit as st
import os
from streamlit_option_menu import option_menu


# Load the trained models
diabetes_model = pickle.load(open('diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
cardiovascular_model = pickle.load(open('cardiovascular_disease_model.sav', 'rb'))
liver_disease_model = pickle.load(open('liver_disease_model.sav', 'rb'))


# Set up the session state to track the selected sidebar option
if 'sidebar_selected' not in st.session_state:
    st.session_state.sidebar_selected = False


# Sidebar options
with st.sidebar:
    selected = option_menu('Disease Prediction',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Cardiovascular Disease Prediction',
                            'Liver Disease Prediction'],
                            icons=['clipboard', 'heart', 'activity', 'droplet'],
                            default_index=0)


# Diabetes Disease Prediction

if selected == 'Diabetes Prediction':

    st.title('Diabetes Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Glucose = st.text_input('Glucose Level (mg/dl)')
    with col3:
        BloodPressure = st.text_input('Blood Pressure (mmHg)')
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    with col2:
        Insulin = st.text_input('Insulin')
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        Pregnancies = st.text_input('Pregnancies')
    with col2:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')

    diabetes_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]
            
            # Make predictions
            diabetes = diabetes_model.predict([user_input])

            if diabetes[0] == 1:
                diabetes_diagnosis = 'High risk of Diabetes'
            else:
                diabetes_diagnosis = 'Low risk of Diabetes'

            st.success(diabetes_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")


# Heart Disease prediction

if selected == 'Heart Disease Prediction':

    st.title('Heart Disease prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (Male:1 / Female:0)')
    with col3:
        trestbps = st.text_input('Blood Pressure (mmHg))')
    with col2:
        cp = st.text_input('Chest Pain (0-3)')
    with col1:
        chol = st.text_input('Cholesterol (mg/dl)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120mg/dl')
    with col1:
        restecg = st.text_input('ECG Result (0-2)')
    with col2:
        thalach = st.text_input('Heart Rate Max')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST Depression')
    with col2:
        slope = st.text_input('ST slope')
    with col3:
        ca = st.text_input('Number of Fluoroscopy vessels (0-3)')
    with col1:
        thal = st.text_input('Thalassemia (0-2)')


    heart_disease_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]
            
            # Make predictions
            heart_disease = heart_disease_model.predict([user_input])

            if heart_disease[0] == 1:
                heart_disease_diagnosis = 'High risk of Heart Disease'
            else:
                heart_disease_diagnosis = 'Low risk of Heart Disease'

            st.success(heart_disease_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")


# Cardiovascular Disease Prediction

if selected == 'Cardiovascular Disease Prediction':

    st.title('Cardiovascular Disease Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        gender = st.text_input('Sex (Male:1 / Female:0)')
    with col3:
        restingBP = st.text_input('Blood Pressure (mmHg)')
    with col1:
        chestpain = st.text_input('Chest Pain (0-3)')
    with col2:
        serumcholestrol = st.text_input('Cholesterol (mg/dl)')
    with col3:
        fastingbloodsugar = st.text_input('Fasting Blood Sugar > 120mg/dl')
    with col1:
        restingelectro = st.text_input('ECG Result (0-2)')
    with col2:
        maxheartrate = st.text_input('Heart Rate Max')
    with col3:
        exerciseangina = st.text_input('Exercise Induced Angina (No:0 / Yes:1)')
    with col1:
        oldpeak = st.text_input('ST Depression')
    with col2:
        slope = st.text_input('ST slope (1-3)')
    with col3:
        noofmajorvessels = st.text_input('Noumber of Fluoroscopy vessels  (0-3)')


    cardiovascular_disease_diagnosis = ''

    if st.button('Cardiovascular Disease Test Result'):
        try:
            user_input = [
                float(age),
                float(gender),
                float(chestpain),
                float(restingBP),
                float(serumcholestrol),
                float(fastingbloodsugar),
                float(restingelectro),
                float(maxheartrate),
                float(exerciseangina),
                float(oldpeak),
                float(slope),
                float(noofmajorvessels)
            ]
            
            # Make predictions
            cardiovascular_disease = cardiovascular_model.predict([user_input])

            if cardiovascular_disease[0] == 1:
                cardiovascular_disease_diagnosis = 'High risk of Cardiovascular Disease'
            else:
                cardiovascular_disease_diagnosis = 'Low risk of Cardiovascular Disease'

            st.success(cardiovascular_disease_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")


# Liver Disease Prediction

if selected == 'Liver Disease Prediction':

    st.title('Liver Disease Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Gender = st.text_input('Sex (Male:0 / Female:1)')
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        AlcoholConsumption = st.text_input('Alcohol Consumption (0-20)')
    with col2:
        Smoking = st.text_input('Smoking (No:0 / Yes:1)')
    with col3:
        GeneticRisk = st.text_input('Genetic Risk (0-2)')
    with col1:
        PhysicalActivity = st.text_input('Physical Activity (0-10)')
    with col2:
        Diabetes = st.text_input('Diabetes (No:0 / Yes:1)')
    with col1:
        Hypertension = st.text_input('Hypertension (No:0 / Yes:1)')
    with col2:
        LiverFunctionTest = st.text_input('Liver Function Test (20-100)')

    Liver_disease_diagnosis = ''

    if st.button('Liver Disease Test Result'):
        try:
            user_input = [
                float(Age),
                float(Gender),
                float(BMI),
                float(Smoking),
                float(AlcoholConsumption),
                float(GeneticRisk),
                float(PhysicalActivity),
                float(Diabetes),
                float(Hypertension),
                float(LiverFunctionTest)
            ]
            
            # Make predictions
            Liver_disease = liver_disease_model.predict([user_input])

            if Liver_disease[0] == 1:
                Liver_disease_diagnosis = 'High risk of Liver Disease'
            else:
                Liver_disease_diagnosis = 'Low risk of Liver Disease'

            st.success(Liver_disease_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")

