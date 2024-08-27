# Multiple Disease Prediction WebApp

This repository contains a Streamlit web application that predicts the risk of four different diseases: Diabetes, Cardiovascular Disease, Heart Disease, and Liver Disease. The app uses machine learning models trained on relevant datasets to provide predictions based on user input.    

  
*Diabetes Low Risk Situation:*
![test1](https://github.com/user-attachments/assets/899b6e3f-295e-4c43-b899-43bf520f02fd)


*Diabetes High Risk Situation:*
![test2](https://github.com/user-attachments/assets/25d9d3eb-c83f-4b71-b686-46137a94ce6d)


## Features
- **User Input:** The app allows users to input various health metrics such as age, gender, BMI, blood pressure, cholesterol levels, blood glucose levels, etc.
- **Disease Risk Prediction:** The app predicts the risk of the following diseases:
  - Diabetes
  - Cardiovascular Disease
  - Heart Disease
  - Liver Disease
- **Interactive UI:** Built with Streamlit, the app provides a user-friendly interface to input data and view predictions.
- **Model Accuracy:** The app uses Logistic Regression and Random Forest classifiers, providing high accuracy in disease risk prediction.

## Datasets
The models were trained on various datasets related to the four diseases:

1. Diabetes Dataset:

- Features: Age, BMI, Blood Pressure, Glucose Level, etc.
- Target: Diabetes risk (1: Yes, 0: No)
  
2. Cardiovascular Disease Dataset:

- Features: Age, Gender, Blood Pressure, Cholesterol, Max Heart Rate, etc.
- Target: Cardiovascular Disease risk (1: Yes, 0: No)

3. Heart Disease Dataset:

- Features: Age, Gender, Chest Pain, Resting Blood Pressure, Serum Cholesterol, etc.
- Target: Heart Disease risk (1: Yes, 0: No)

4. Liver Disease Dataset:

- Features: Age, Gender, BMI, Alcohol Consumption, Liver Function Test Results, etc.
- Target: Liver Disease risk (1: Yes, 0: No)
  
## Usage
1. Open the app in your browser (usually at `http://localhost:8501`)
2. Select the disease for which you want to predict the risk.
3. Enter the required health metrics.
4. Click the "Test Result" button to see the risk prediction.

## Model Training
The machine learning models were trained using the following libraries:

- **Pandas:** For data manipulation and analysis.
- **Scikit-learn:** For model training and evaluation.
- **Pickle:** For saving and loading trained models.
The models were trained on different datasets with a focus on maximizing accuracy. The Random Forest Classifier was used for its robustness and high accuracy.

## Conclusion

This kind of a project is crucial as it leverages machine learning to predict disease risk, enabling early detection and timely intervention. By identifying high-risk individuals, it can significantly improve patient outcomes, optimize resource allocation, and enhance overall healthcare efficiency.

For any questions or further assistance, please feel free to contact me.

Dhananjaya Mudunkotuwa  
dhananjayamudunkotuwa1998@gmail.com 
