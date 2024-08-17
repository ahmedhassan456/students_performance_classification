import streamlit as st
from controller.LoadModel import LoadModel
from controller.GetPredictions import GetPredictions

gender_options = ["Male", "Female"]
ethnicity_options = ["Caucasian", "African American", "Asian", "Other"]
parental_education_options = ["None", "High School", "Some College", "Bachelor's", "Higher"]
yes_no_options = ["No", "Yes"]
parental_support_options = ["None", "Low", "Moderate", "High", "Very High"]

st.title("Student Performance Prediction App")
st.write("Enter the Student Info:")

age = st.number_input("Student Age: ", min_value=15, max_value=18, step=1)
gender = st.selectbox("Student Gender: ", gender_options)
ethnicity = st.selectbox("Student Ethnicity: ", ethnicity_options)
parental_education = st.selectbox("Parental Education: ", parental_education_options)
study_time_weekly = st.number_input("Study Time Weekly: ", min_value=0, max_value=20, step=1)
absences = st.number_input("Absences: ", min_value=0, max_value=30, step=1)
tutoring = st.selectbox("Tutoring: ", yes_no_options)
parental_support = st.selectbox("Parental Support: ", parental_support_options)
extracurricular = st.selectbox("Extracurricular: ", yes_no_options)
sports = st.selectbox("Sports: ", yes_no_options)
music = st.selectbox("Music: ", yes_no_options)
volunteering = st.selectbox("Volunteering: ", yes_no_options)
gpa = st.number_input("Student GPA: ", min_value=2.0, max_value=4.0, step=0.01)

model = LoadModel("model/model.pkl")
list_of_features = [age, gender, ethnicity, parental_education, study_time_weekly, absences, tutoring, 
                    parental_support, extracurricular, sports, music, volunteering, gpa]

if st.button("Predict"):
    prediction = GetPredictions(model, list_of_features)

    st.write(f"The Predicted Grad Class is: {prediction}")