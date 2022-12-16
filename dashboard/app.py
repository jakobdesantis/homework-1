#-------------------#
# SETUP
import streamlit as st

import numpy as np
import pandas as pd
import altair as alt

from pathlib import Path
import datetime as dt
from datetime import datetime

#-------------------
# DATA

# Data import
#df = pd.read_csv('/Users/User/Documents/GitHub/homework-1/data/external/data.csv')
#df = pd.read_csv('../data/external/data.csv')
#df = pd.read_csv('https://github.com/jakobdesantis/homework-1/blob/main/data/external/data.csv')
df = pd.read_csv('https://raw.githubusercontent.com/jakobdesantis/homework-1/main/data/external/data.csv?token=GHSAT0AAAAAABZZVTDROHOMKD4MZSBLNI2QY445DAQ')

# Data transformation
#-----------
df2 = df.drop(labels=range(5000, 250000), axis=0)
#-----------
df2["length"] = df2["content"].str.len()
#----------
df2['publish_date']= pd.to_datetime(df2['publish_date']).dt.date
df2['publish_date'] = pd.to_datetime(df2['publish_date'])

#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Make a sidebar
chart_language = st.sidebar.multiselect('Wie schätzt du deine Bildschirmzeit pro Tag ein?', 0, 10, 1)
#Text noch bearbeiten

#-------------------
# HEADER

# Title of our app
st.title("Allgemeiner Titel")
# Add header
st.header("This is my interactive app from team D")

#-------------------
# BODY

#-------------------
# Häufigste Länder
st.subheader("Häufigste Länder")
st.write("Here's my data:")

source = df2

chart_region = alt.Chart(source).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("count(region)", type="quantitative"),
    color=alt.Color("region", type="nominal")
).properties(
    title='Anteil der verschiedenen Länder',
    width=400,
    height=300
)

chart_region.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)
c = chart_region

# Show plot
st.altair_chart(c, use_container_width=True)

#restliche Graphen einfügen (in anderer Datei vorbeireitet)