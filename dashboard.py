# Import the necessary modules
#27th August

import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd

#Load and prepare the data
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['Species'] = iris.target
df['Species'] = df['Species'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

#Sidebar from user input
st.sidebar.header('Input Features')

def user_input_features():
    sepal_length = st.sidebar.slider('sepal length (cm)', float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
    sepal_width = st.sidebar.slider('sepal width (cm)', float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
    petal_length = st.sidebar.slider('petal length (cm)', float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
    petal_width = st.sidebar.slider('petal width (cm)', float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

    data = {'sepal length (cm)' : sepal_length,
            'sepal width (cm)' : sepal_width,
            'petal length (cm)' : petal_length,
            'petal width (cm)' : petal_width
            }
    
    features = pd.DataFrame(data,index= [0])
    #Data is the values and start from index 0
    return features

input_df = user_input_features()

#Main Panel
st.write("# Iris Flower Prediction")

#Combine the input features with the entire Dataset
iris_raw = df.drop(columns=['Species'])
iris_raw = pd.concat([input_df, iris_raw], axis=0)

#Standarize the input features
scaler = StandardScaler()
iris_raw_scaled = scaler.fit_transform(iris_raw)
input_scaled = iris_raw_scaled[:1] #Select only the user input

#In real world scenario we first train the model then load the data so we train it first
#Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(iris_raw_scaled[1:], df['Species'])

#Prediction 
prediction = model.predict(input_scaled)
prediction_proba = model.predict_proba(input_scaled)

st.subheader("Prediction")
#st.write(iris.target_names[prediction])

st.subheader("Prediction Probability")
st.write(prediction_proba)


#Predictions based on the slider inputs, which flower huna sakcha vanera predict garcha as we move the slider value
#Slider ko satta we can also use text input fields to male predictions
