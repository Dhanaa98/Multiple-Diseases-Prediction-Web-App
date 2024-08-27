import pickle
import streamlit as st
import os
from streamlit_option_menu import option_menu


# Load the trained models
diabetes_model = pickle.load(open('Models/diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open('Models/heart_disease_model.sav', 'rb'))
cardiovascular_model = pickle.load(open('Models/cardiovascular_disease_model.sav', 'rb'))
liver_disease_model = pickle.load(open('Models/liver_disease_model.sav', 'rb'))


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
        age = st.text_input('Age')
    with col2:
        gender = st.selectbox('Gender', options = ['Male', 'Female', 'Other'])
    with col3:
        hypertension = st.selectbox('Hyper Tension', options = ['No', 'Yes'])
    with col1:
        heart_disease = st.selectbox('Heart Disease', options = ['No', 'Yes'])
    with col2:
        smoking_history = st.selectbox('Smoking History', options = ['Non-Smoker', 'Smoker'])
    with col3:
        bmi = st.text_input('BMI')
    with col1:
        HbA1c_level = st.text_input('HbA1c Level')
    with col2:
        blood_glucose_level = st.text_input('Blood Glucose Level')

    diabetes_diagnosis = ''

    if st.button('Diabetes Test Result'):

        # Mapping
        gender_map = {'Female': 0, 'Male': 1, 'Other': 2}
        gender_value = gender_map[gender]
        
        hypertension_map = {'Yes': 1, 'No': 0}
        hypertension_value = hypertension_map[hypertension]

        heart_disease_map = {'Yes': 1, 'No': 0}
        heart_disease_value = heart_disease_map[heart_disease]

        smoking_history_map = {'Smoker': 1, 'Non-Smoker': 0}
        smoking_history_value = smoking_history_map[smoking_history]

        try:
            user_input = [
                float(age),
                float(gender_value),
                float(hypertension_value),
                float(heart_disease_value),
                float(smoking_history_value),
                float(bmi),
                float(HbA1c_level),
                float(blood_glucose_level)
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
        sex = st.selectbox('Gender', options = ['Male', 'Female'])
    with col3:
        trestbps = st.text_input('Blood Pressure (mmHg))')
    with col2:
        cp = st.selectbox('Chest Pain', options = ['No pain', 'Typical angina', 'Atypical angina', 'Non-anginal pain'])
    with col1:
        chol = st.text_input('Cholesterol (mg/dl)')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar', options = ['Above 120 mg/dL', 'Below 120 mg/dL'])
    with col1:
        restecg = st.selectbox('ECG Result', options = ['Normal', 'ST-T wave abnormality', 'Ventricular hypertrophy'])
    with col2:
        thalach = st.text_input('Heart Rate Max')
    with col3:
        exang = st.selectbox('Exercised Induced Angina', options = ['No', 'Yes'])
    with col1:
        oldpeak = st.text_input('ST Depression')
    with col2:
        slope = st.selectbox('ST Slope', options = ['Flat', 'Upsloping', 'Downsloping'])
    with col3:
        ca = st.selectbox('Number of Fluoroscopy vessels', options = ['0', '1', '2', '3'])
    with col1:
        thal = st.selectbox('Thalassemia', options = ['Normal', 'Fixed defect', 'Reversible defect'])


    heart_disease_diagnosis = ''

    if st.button('Heart Disease Test Result'):

        # Mapping
        gender_map = {'Female': 0, 'Male': 1}
        gender_value = gender_map[sex]

        chestpain_map = {'No pain':3, 'Typical angina':0, 'Atypical angina':1, 'Non-anginal pain':2}
        chestpain_value = chestpain_map[cp]
        
        fastingbloodsugar_map = {'Above 120 mg/dL':1, 'Below 120 mg/dL':0}
        fastingbloodsugar_value = fastingbloodsugar_map[fbs]
        
        ECG_result_map = {'Normal':0, 'ST-T wave abnormality':1, 'Ventricular hypertrophy':1}
        ECG_result_value = ECG_result_map[restecg]
        
        exerciseangina_map = {'Yes': 1, 'No': 0}
        exerciseangina_value = exerciseangina_map[exang]
        
        slope_map = {'Upsloping':0,'Flat':1, 'Downsloping':2}
        slope_value = slope_map[slope]

        fluoroscopy_map = {'0':0,'1':1, '2':2, '3':3}
        fluoroscopy_value = fluoroscopy_map[ca]

        Thalassemia_map = {'Normal':2, 'Fixed defect':1, 'Reversible defect':3}
        Thalassemia_value = Thalassemia_map[thal]

        try:
            user_input = [
                float(age),
                float(gender_value),
                float(chestpain_value),
                float(trestbps),
                float(chol),
                float(fastingbloodsugar_value),
                float(ECG_result_value),
                float(thalach),
                float(exerciseangina_value),
                float(oldpeak),
                float(slope_value),
                float(fluoroscopy_value),
                float(Thalassemia_value)
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
        gender = st.selectbox('Gender', options = ['Male', 'Female'])
    with col3:
        restingBP = st.text_input('Blood Pressure (mmHg)')
    with col1:
        chestpain = st.selectbox('Chest Pain', options = ['No pain', 'Typical angina', 'Atypical angina', 'Non-anginal pain'])
    with col2:
        serumcholestrol = st.text_input('Cholesterol (mg/dl)')
    with col3:
        fastingbloodsugar = st.selectbox('Fasting Blood Sugar', options = ['Above 120 mg/dL', 'Below 120 mg/dL'])
    with col1:
        restingelectro = st.selectbox('ECG Result', options = ['Normal', 'ST-T wave abnormality', 'Ventricular hypertrophy'])
    with col2:
        maxheartrate = st.text_input('Heart Rate Max')
    with col3:
        exerciseangina = st.selectbox('Exercised Induced Angina', options = ['No', 'Yes'])
    with col1:
        oldpeak = st.text_input('ST Depression')
    with col2:
        slope = st.selectbox('ST Slope', options = ['Upsloping','Flat', 'Downsloping'])
    with col3:
        noofmajorvessels = st.selectbox('Number of Fluoroscopy vessels', options = ['0', '1', '2', '3'])


    cardiovascular_disease_diagnosis = ''

    if st.button('Cardiovascular Disease Test Result'):

        # Mapping
        gender_map = {'Female': 0, 'Male': 1}
        gender_value = gender_map[gender]

        chestpain_map = {'No pain':3, 'Typical angina':0, 'Atypical angina':1, 'Non-anginal pain':2}
        chestpain_value = chestpain_map[chestpain]
        
        fastingbloodsugar_map = {'Above 120 mg/dL':1, 'Below 120 mg/dL':0}
        fastingbloodsugar_value = fastingbloodsugar_map[fastingbloodsugar]
        
        ECG_result_map = {'Normal':0, 'ST-T wave abnormality':1, 'Ventricular hypertrophy':1}
        ECG_result_value = ECG_result_map[restingelectro]
        
        exerciseangina_map = {'Yes': 1, 'No': 0}
        exerciseangina_value = exerciseangina_map[exerciseangina]
        
        slope_map = {'Upsloping':0,'Flat':1, 'Downsloping':2}
        slope_value = slope_map[slope]

        fluoroscopy_map = {'0':0,'1':1, '2':2, '3':3}
        fluoroscopy_value = fluoroscopy_map[noofmajorvessels]

        try:
            user_input = [
                float(age),
                float(gender_value),
                float(chestpain_value),
                float(restingBP),
                float(serumcholestrol),
                float(fastingbloodsugar_value),
                float(ECG_result_value),
                float(maxheartrate),
                float(exerciseangina_value),
                float(oldpeak),
                float(slope_value),
                float(fluoroscopy_value)
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
        Gender = st.selectbox('Gender', options = ['Male', 'Female'])
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        AlcoholConsumption = st.text_input('Alcohol Consumption (0-20)')
    with col2:
        Smoking = st.selectbox('Smoking History', options = ['Non-Smoker', 'Smoker'])
    with col3:
        GeneticRisk = st.selectbox('Genetic Risk', options = ['0', '1', '2'])
    with col1:
        PhysicalActivity = st.text_input('Physical Activity (0-10)')
    with col2:
        Diabetes = st.selectbox('Diabetes', options = ['No', 'Yes'])
    with col1:
        Hypertension = st.selectbox('Hyper Tension', options = ['No', 'Yes'])
    with col2:
        LiverFunctionTest = st.text_input('Liver Function Test (20-100)')

    Liver_disease_diagnosis = ''

    if st.button('Liver Disease Test Result'):

        # Mapping
        gender_map = {'Female': 1, 'Male': 0}
        gender_value = gender_map[Gender]

        smoking_history_map = {'Smoker': 1, 'Non-Smoker': 0}
        smoking_history_value = smoking_history_map[Smoking]

        GeneticRisk_map = {'0':0, '1': 1, '2': 2}
        GeneticRisk_value = GeneticRisk_map[GeneticRisk]

        diabetes_map = {'Yes': 1, 'No': 0}
        diabetes_value = diabetes_map[Diabetes]

        hypertension_map = {'Yes': 1, 'No': 0}
        hypertension_value = hypertension_map[Hypertension]

        try:
            user_input = [
                float(Age),
                float(gender_value),
                float(BMI),
                float(smoking_history_value),
                float(AlcoholConsumption),
                float(GeneticRisk_value),
                float(PhysicalActivity),
                float(diabetes_value),
                float(hypertension_value),
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

