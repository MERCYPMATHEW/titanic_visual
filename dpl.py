#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Titanic_Dataset")

#import dataset
df = pd.read_csv('titanic.csv')
#First thirty rows
titanic = df.head(30)
#Display the table
st.table(titanic)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
titanic.plot(kind='bar')
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(titanic['Fare'])
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='Age',y='Fare',data=titanic,kind='hex')
st.pyplot()
#pairplot
st.subheader("Pairplot")
sns.pairplot(titanic,hue='Sex',palette='rainbow')
st.pyplot()
#Rugplot
st.subheader("Rugplot")
sns.rugplot(titanic['Fare'])
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(titanic.corr(),cmap='coolwarm',annot=True)
st.pyplot()
