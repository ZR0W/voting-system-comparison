import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

@st.cache
def get_data():
    # get data and store
    range = 50
    num_points = 100
    data = pd.DataFrame(np.random.randint(-range, range, size=(num_points, 2)), columns=list('XY'))
    return data

df = get_data()

st.title("Political Spectrum Voting Method Simulation")
st.markdown("markdown text")

st.header("header")
st.markdown("more mark down text")

st.dataframe(df)
st.markdown(df.size)

fig = px.scatter(df, x="X", y="Y")
st.plotly_chart(fig)