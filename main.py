import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")

df = pd.read_csv("happy.csv")

data_for_axis = list(df.columns)[1:]
data_for_x_axis_select = [columns.capitalize().replace('_'," ") for columns in data_for_axis]
data_for_y_axis_select = [columns.capitalize().replace('_'," ") for columns in data_for_axis]

x_axis = st.selectbox("Select the data for the X-axis",options=data_for_x_axis_select)
y_axis = st.selectbox("Select the data for the Y-axis",options=data_for_y_axis_select)

st.title(f"{x_axis} and {y_axis}")

data_for_x_axis = df[f"{x_axis.lower().replace(' ','_')}"]
data_for_y_axis = df[f"{y_axis.lower().replace(' ','_')}"]


figure = px.scatter(x=data_for_x_axis,y=data_for_y_axis,labels={"x":f"{x_axis}", "y":f"{y_axis}"})

st.plotly_chart(figure)