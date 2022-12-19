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
#df = pd.read_csv('C:\Users\User\Documents\Studium\Medienmanagement\HdM Stuttgart\Semester 4\BigData\data.csv')
#df = pd.read_csv('../data/external/data2.csv')
#df = pd.read_csv('C:/Users/User/Documents/GitHub/homework-1/data/external/data.csv')
#df = pd.read_csv('C:\Users\User\Downloads\homework-1-main\homework-1-main\data\external\data.csv')
#df = pd.read_csv('https://raw.githubusercontent.com/jakobdesantis/homework-1/main/data/external/data.csv')
#df = pd.read_csv('https://raw.githubusercontent.com/jakobdesantis/homework-1/main/data/external/data2.csv')
#df = pd.read_csv('https://raw.githubusercontent.com/jakobdesantis/homework-1/main/data/external/data3.csv')
df = pd.read_csv('../data/external/data2.csv')
df2 = df


# Data transformation
#df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
#-----------
df2["length"] = df2["content"].str.len()
#----------
df2['publish_date']= pd.to_datetime(df2['publish_date']).dt.date
df2['publish_date'] = pd.to_datetime(df2['publish_date'])

#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Header
st.sidebar.header("This is my sidebar")

# Make a sidebar
#chart_language = st.sidebar.multiselect('Wie schätzt du deine Bildschirmzeit pro Tag ein?', 0, 10, 1)
chart_language = st.sidebar.multiselect('Select language', df['language'].unique().tolist())
#Text noch bearbeiten

# Show output of slider selection
st.sidebar.write("My life satisfaction is around ", chart_language, 'points')

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


#-------------------
# Häufigste Sprachen
st.subheader("Häufigste Sprachen")
st.write("Here's my data:")

source = df2

chart_language = alt.Chart(source).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("count(language)", type="quantitative"),
    color=alt.Color("language", type="nominal", title='Sprachen')
).properties(
    title='Anteil der verschiedenen Sprachen',
    width=400,
    height=300
)

chart_language.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)
c= chart_language

# Show plot
st.altair_chart(c, use_container_width=True)


#-------------------
# Followerverteilung
st.subheader("Followerverteilung")
st.write("Here's my data:")

source = df2

chart_followers = alt.Chart(source).mark_bar().encode(
  x=alt.X('author',
    title="Account-Name",
    sort="-y"
  ),
  y=alt.Y('max(following)',
    title="Anzahl Follower"
  ),
  color=alt.Color("author",
    type="nominal",
    title='Account',
    legend=None),
  tooltip=(
        alt.Tooltip("max(following)", title="Follower")
  )
).properties(
    title='Accounts mit den meisten Followern',
    width=800,
    height=300,
)

chart_followers.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)
c= chart_followers

# Show plot
st.altair_chart(c, use_container_width=True)


#-------------------
# Posts je nach Zeit
st.subheader("Posts je nach Zeit")
st.write("Here's my data:")

source = df2

chart_time = alt.Chart(source).mark_line().encode(
    x=alt.X("date",
        title="Datum"
    ),
    y=alt.Y("count(date)",
        title="Anzahl der Tweets"
    ),
    tooltip=(
        alt.Tooltip("count(date)", title="Anzahl der Tweets")
    )
).properties(
    title='Anzahl der Tweets pro Tag',
    width=800,
    height=300
)

chart_time.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)
c= chart_time

# Show plot
st.altair_chart(c, use_container_width=True)


#-------------------
# Tweets nach Wochentag und Uhrzeit
st.subheader("Tweets nach Wochentag und Uhrzeit")
st.write("Here's my data:")

source = df2

heatmap = alt.Chart(df2).mark_rect().encode(
    x=alt.X("hour",
        title="Uhrzeit"
    ),
    y=alt.Y('weekday_name',
            title="Wochentag",
            type='nominal',
            sort=weekday_names
           ),
    color=alt.Color("count(weekday_name)",
    legend=None),
    tooltip=(
        alt.Tooltip("count(weekday_name)", title="Anzahl der Tweets")
    )
).properties(
    title='Tweets nach Wochentag und Uhrzeit',
    width=1000,
    height=300
)

heatmap.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)
c= heatmap

# Show plot
st.altair_chart(c, use_container_width=True)

