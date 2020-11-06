import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import copy

# The following customization requires upgraded streamlit
# st.beta_set_page_config(
#     page_title="Voting System Simulation",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# @st.cache(allow_output_mutation=True)
def get_data():
    # get data and store
    data = pd.read_csv("random_xy_data.csv")
    return data

# beware cache mutation issue
# recourse: https://docs.streamlit.io/en/stable/troubleshooting/caching_issues.html

data = get_data()
df = data.copy()
# df = copy.deepcopy(get_data())

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

st.header("First Election Method: Instant Run-Off Elections")
st.markdown("The first election method we will look at is the instant run-off election.")
st.markdown("Simply put, we let everyone choose which candidate they like best. And in the end, we count all the votes to see which candidate has the most votes.")
st.markdown("let's create two imaginary candidates: Donavan Turn & James Byron")
st.markdown("and here is where they lie on our political spectrum: ")
candidate_one = (50, 70)
candidate_two = (-40, -20)
candidate_three = (-50, -10)

new_fig = fig
new_fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[candidate_one[0]],
        y=[candidate_one[1]],
        marker=dict(
            color='rgba(178,34,34,0.3)',
            size=30,
            line=dict(
                color='DarkSlateBlue',
                width=1
            )
        ),
        text="Candidate One",
        showlegend=False
    )
)
new_fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[candidate_two[0]],
        y=[candidate_two[1]],
        marker=dict(
            color='rgba(0,128,0,0.3)',
            size=30,
            line=dict(
                color='DarkSlateBlue',
                width=1
            )
        ),
        text="Candidate Two",
        showlegend=False
    )
)
new_fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[candidate_three[0]],
        y=[candidate_three[1]],
        marker=dict(
            color='rgba(255,127,80,0.3)',
            size=30,
            line=dict(
                color='DarkSlateBlue',
                width=1
            )
        ),
        text="Candidate Three",
        showlegend=False
    )
)

st.plotly_chart(new_fig)

# use this to do that extra point on scatter plot thing:
# https://plotly.com/python/marker-style/

st.markdown("In this simplified graph, everyone would simply vote for the candicate closest to them on the political spectrum, being the one they agree with the msot.")

df_copy = df.copy()
# denoting the first candidate as A, and the second one as B
df_copy["distance_to_A"] = np.sqrt((df_copy["x_preference"]-candidate_one[0])**2 + (df_copy["y_preference"]-candidate_one[1])**2)
df_copy["distance_to_B"] = np.sqrt((df_copy["x_preference"]-candidate_two[0])**2 + (df_copy["y_preference"]-candidate_two[1])**2)
df_copy["distance_to_C"] = np.sqrt((df_copy["x_preference"]-candidate_three[0])**2 + (df_copy["y_preference"]-candidate_three[1])**2)


# df_copy["instant_run_off_choice"] = np.where(
#     df_copy["distance_to_A"] < df_copy["distance_to_B"],
#     "A",
#     "B")

def compare_distance(row):
    min_distance = min(row["distance_to_A"], row["distance_to_B"], row["distance_to_C"])
    if row["distance_to_A"] == min_distance:
        return "A"
    elif row["distance_to_B"] == min_distance:
        return "B"
    elif row["distance_to_C"] == min_distance:
        return "C"
    else:
        return "NA"

df_copy["instant_run_off_choice"] = df_copy.apply(compare_distance, axis=1)

st.write(df_copy.head())
print(id(data))
print(id(df))
print(id(df.copy))
# TODO: dataframe mutation issue needs resolved

st.markdown("We've now done some quick math to compute how close every point is to out two candicates. Through comparison, we know now how everyone is voting in the instand runoff election. If we plot that out to visualize it: ")

fig_runoff = px.scatter(df_copy, x="x_preference", y="y_preference", color="instant_run_off_choice", 
    labels={
        "x_preference": "Apples(-) or Oranges(+)", 
        "y_preference": "Pizza: With(-) or Without(+) Pineapple"
    }, 
    title="Population Political Spectrum Distribution",
    hover_data=["distance_to_A", "distance_to_B"]
)
fig_runoff.update_traces(
    marker=dict(
        size=7,
        line=dict(width=2, color="DarkSlateGrey")
    ),
    selector=dict(mode="markers")
)
st.plotly_chart(fig_runoff)

# https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2