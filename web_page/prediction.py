import pandas as pd
import joblib
import streamlit as st

model_path = 'C:\\userspace\\daya\\python\\proj\\web_page\\random_forest_model.joblib'
model = joblib.load(model_path)

def predict_page():

    def preprocess_input(value):
        if value == 'Usually' or value == 'Yes':
            return 0
        elif value == 'Sometimes' or value == 'No':
            return 1
        elif value == 'Seldom':
            return 2
        elif value == 'Most-Often':
            return 3

    # Function to predict diagnosis
    def predict_diagnosis(input_data):
        # Make prediction
        predicted_class = model.predict(input_data)
        # Define a dictionary to map class labels to diagnoses
        diagnosis_mapping = {
            0: 'Depression',
            1: 'Bipolar Type-1',
            2: 'Bipolar Type-2',
            3: 'Normal'
        }
        # Return the predicted diagnosis
        return diagnosis_mapping[predicted_class[0]]

    # Create input fields for user input
    st.markdown("<p style='font-family: Georgia, serif; color:#EB0446; font-size:30px;'>Enter the details for the following:</p>", unsafe_allow_html=True)
    sadness = preprocess_input(st.selectbox('Sadness', ['Usually', 'Sometimes', 'Seldom', 'Most-Often']))
    euphoric = preprocess_input(st.selectbox('Euphoric', ['Usually', 'Sometimes', 'Seldom', 'Most-Often']))
    exhausted = preprocess_input(st.selectbox('Exhausted', ['Usually', 'Sometimes', 'Seldom', 'Most-Often']))
    sleep_disorder = preprocess_input(st.selectbox('Sleep Disorder', ['Usually', 'Sometimes', 'Seldom', 'Most-Often']))
    mood_swing = preprocess_input(st.radio('Mood Swing', ['Yes', 'No']))
    suicidal_thoughts = preprocess_input(st.radio('Suicidal Thoughts', ['Yes', 'No']))
    anorexia = preprocess_input(st.radio('Anorexia', ['Yes', 'No']))
    authority_respect = preprocess_input(st.radio('Authority Respect', ['Yes', 'No']))
    try_explanation = preprocess_input(st.radio('Try-Explanation', ['Yes', 'No']))
    aggressive_response = preprocess_input(st.radio('Aggressive Response', ['Yes', 'No']))
    ignore_move_on = preprocess_input(st.radio('Ignore & Move-On', ['Yes', 'No']))
    nervous_breakdown = preprocess_input(st.radio('Nervous Breakdown', ['Yes', 'No']))
    admit_mistakes = preprocess_input(st.radio('Admit Mistakes', ['Yes', 'No']))
    overthinking = preprocess_input(st.radio('Overthinking', ['Yes', 'No']))
    sexual_activity = st.slider('Sexual Activity', min_value=0, max_value=10, value=0)
    concentration = st.slider('Concentration', min_value=0, max_value=10, value=0)
    optimism = st.slider('Optimism', min_value=0, max_value=10, value=0)

    # Create a button to trigger prediction and save data
    if st.button('Predict Diagnosis'):
        # Format input data
        input_data = {
            'Sadness': [sadness],
            'Euphoric': [euphoric],
            'Exhausted': [exhausted],
            'Sleep disorder': [sleep_disorder],
            'Mood Swing': [mood_swing],
            'Suicidal thoughts': [suicidal_thoughts],
            'Anorexia': [anorexia],
            'Authority Respect': [authority_respect],
            'Try-Explanation': [try_explanation],
            'Aggressive Response': [aggressive_response],
            'Ignore & Move-On': [ignore_move_on],
            'Nervous Break-down': [nervous_breakdown],
            'Admit Mistakes': [admit_mistakes],
            'Overthinking': [overthinking],
            'Sexual Activity': [sexual_activity],
            'Concentration': [concentration],
            'Optimism': [optimism]
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame(input_data)
        # Make prediction
        prediction = predict_diagnosis(input_df)
        # Display the predicted diagnosis
        st.write(f'Predicted Diagnosis: {prediction}')

        # Save user input data to CSV
        input_df.to_csv('user_input_data.csv', index=False)

