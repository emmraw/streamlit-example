from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import plotly.express as px
import datetime
import time
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

st.title("Practise Streamlit")
st.header('Practise widgets')

d = st.date_input(
     "Enter today's date",
     datetime.date(2020,3,21))
st.write("Today's date is:", d)

option1 = st.selectbox(
     "What is today's weather like?",
     ('Sunny', 'Cloudy', 'Rainy'))
     
option2 = st.selectbox("Is it a bank holiday today?",('No','Yes'))
                     
option3 = st.selectbox("Is there a special event today?",('No','Yes'))
     
st.write("You chose: ", option1, option2, option3)

add_selectbox = st.sidebar.selectbox(
    "Is it a bank holiday?",
    ("No","Yes"))

add_selectbox = st.sidebar.selectbox(
    ["Is it a bank holiday?","Is there a special event?"]
    ("No","Yes"),("No","Yes"))

