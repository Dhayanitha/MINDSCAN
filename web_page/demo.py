import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_path = 'C:\\userspace\\daya\\python\\proj\\random_forest_model.joblib'
model = joblib.load(model_path)

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

# Streamlit web app
def main():
    # Set the title of the web app
    st.title('Mental Health Diagnosis Predictor')

    # Create input fields for user input
    st.header('Enter Patient Data')
    sadness = st.number_input('Sadness', value=0)
    euphoric = st.number_input('Euphoric', value=0)
    exhausted = st.number_input('Exhausted', value=0)
    sleep_disorder = st.number_input('Sleep Disorder', value=0)
    mood_swing = st.number_input('Mood Swing', value=0)
    suicidal_thoughts = st.number_input('Suicidal Thoughts', value=0)
    anorexia = st.number_input('Anorexia', value=0)
    authority_respect = st.number_input('Authority Respect', value=0)
    try_explanation = st.number_input('Try-Explanation', value=0)
    aggressive_response = st.number_input('Aggressive Response', value=0)
    ignore_move_on = st.number_input('Ignore & Move-On', value=0)
    nervous_breakdown = st.number_input('Nervous Breakdown', value=0)
    admit_mistakes = st.number_input('Admit Mistakes', value=0)
    overthinking = st.number_input('Overthinking', value=0)
    sexual_activity = st.number_input('Sexual Activity', value=0)
    concentration = st.number_input('Concentration', value=0)
    optimism = st.number_input('Optimism', value=0)

    # Create a button to trigger prediction
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

# Run the Streamlit web app
if __name__ == '__main__':
    main()
