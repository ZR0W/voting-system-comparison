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

# page layout
st.title("Political Spectrum Voting Method Simulation")
st.markdown("First let's create a very simplified view rerpesenting the political preferences of a population")

st.header("The Data")
st.markdown("here we have a set of random x-y coordinate data")
st.dataframe(df)
st.markdown(df.shape)
st.markdown(df.columns)

st.markdown("let's plot that on a graph to visualize it")
fig = px.scatter(df, x="x_preference", y="y_preference", 
    labels={
        "x_preference": "Apples(-) or Oranges(+)", 
        "y_preference": "Pizza: With(-) or Without(+) Pineapple"
    }, 
    title="Population Political Spectrum Distribution"
)
fig.update_traces(
    marker=dict(
        size=7,
        line=dict(width=2, color="DarkSlateGrey")
    ),
    selector=dict(mode="markers")
)
st.plotly_chart(fig)

st.markdown("Great! In this simplified society, there are only two important issues: ")
st.markdown("weather or not pineapple belongs on pizza, shown by the y-axis, ")
st.markdown("and which is better: apples or oragnes, shown by the x-axis")
st.markdown("this map gives you an idea of how strongly our population feels about each subject, and where they fall on the political spectrum.")

st.header("First Method: TODO i forgot what it was called???")
st.markdown("the first blah blah blah")
# https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2