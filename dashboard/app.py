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
df = pd.read_csv('https://github.com/jakobdesantis/homework-1/blob/main/data/external/data.csv')

# Data transformation
df['Date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')



#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Make a chart_language
chart_language = st.sidebar.multiselect('Select language', 0, 10, 1)

#-------------------
# HEADER

# Title of our app
st.title("Verteilung der Sprachen")
# Add header
st.header("This is my interactive app from team D")

#-------------------
# BODY

#-------------------
# Show static DataFrame
st.subheader("Show Data")
st.write("Here's my data:")

language_count = df2['language'].value_counts(normalize=True, sort=True)
df_language = language_count.to_frame()
df_language = df_language.rename_axis("Language")
df_language = df_language.reset_index()
df_language.columns = ["language", "percentage"]
df_language['percentage'] = df_language['percentage'].multiply(100)

source = df_language

chart_language = alt.Chart(source).mark_bar().encode(
  x=alt.X('language',
    sort='-y',
    title="Sprache"
  ),
  y=alt.Y('percentage',
    title="Anteil in %"
  ),
  color=alt.Color("language:N", type="nominal")
).properties(
    title='Verteilung der Sprachen',
    width=600,
    height=300
)

chart_language.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)

# Show plot
st.altair_chart(c, use_container_width=True)

#-------------------
# Show a map
st.write("Plot a map")
st.map(df_language)

#-------------------