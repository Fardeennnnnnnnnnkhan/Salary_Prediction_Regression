import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf       

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

# Load the trained model
model = tf.keras.models.load_model('regression_model.h5')

# Load the encoders and scaler
with open('label_encoder_gender2.pkl', 'rb') as file:
    label_encoder_gender_2 = pickle.load(file)

with open('one_hot_encoder2.pkl', 'rb') as file:
    one_hot_encoder2 = pickle.load(file)

with open('scaler2.pkl', 'rb') as file:
    scaler2 = pickle.load(file)


#Stream Lit App
st.title("Estimated Salary Prediction")

#User Input 
geography = st.selectbox("Geography", one_hot_encoder2.categories_[0])
gender = st.selectbox('Gender' , label_encoder_gender_2.classes_)
age = st.slider('Age' , 18 , 92 )
balance = st.number_input('Balance')
creditscore = st.number_input('Credit Score')
tenure = st.slider('Tenure' , 0 , 10)
num_of_products = st.slider('Number of Products' , 1 , 4)
has_cr_card = st.selectbox('Has Credit Card' , [0 , 1])
is_active_member = st.selectbox('Is Active Member' , [0 , 1])
Exited= st.selectbox('Exited' , [0 , 1])

#Prepare the Input Data
input_data = pd.DataFrame({
    'CreditScore': [creditscore],
    'Gender':[label_encoder_gender_2.transform([gender])[0]],
    'Age':[age],
    'Tenure':[tenure],
    'Balance':[balance],
    'NumOfProducts':[num_of_products],
    'HasCrCard':[has_cr_card],
    'IsActiveMember':[is_active_member],
    'Exited':[Exited]
})

#One Hot Encode 'Geography'
geo_encoder = one_hot_encoder2.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoder,columns = one_hot_encoder2.get_feature_names_out(['Geography']))

#Combine Input Data with Encoded Geography
input_data = pd.concat([input_data.reset_index(drop=True ) , geo_encoded_df] , axis = 1)

#Scale the Input Data

input_data_scaled = scaler2.transform(input_data)

#Predict churn

prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

st.write(f'Estimated Salary : {prediction_proba : 2f}')
