import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# The following customization requires upgraded streamlit
# st.beta_set_page_config(
#     page_title="Voting System Simulation",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

@st.cache
def get_data():
    # get data and store
    data = pd.read_csv("random_xy_data.csv")
    return data

df = get_data()

st.title("Political Spectrum Voting Method Simulation")
st.markdown("markdown text")

st.header("header")
st.markdown("more mark down text")

st.dataframe(df)
st.markdown(df.shape)
st.markdown(df.columns)

fig = px.scatter(df, x="x_preference", y="y_preference")
st.plotly_chart(fig)

# https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2