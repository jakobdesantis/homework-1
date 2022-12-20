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
df.drop(df.columns[[0, 1, 2, 3, 5, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]], axis=1, inplace=True)
df['publish_date'] = pd.to_datetime(df['publish_date'], format='%m/%d/%Y %H:%M')
#-----------
#df2["length"] = df2["content"].str.len()
#----------
#df2['publish_date']= pd.to_datetime(df2['publish_date']).dt.date
#df2['publish_date'] = pd.to_datetime(df2['publish_date'])
#df2['date'] = pd.to_datetime(df2['publish_date'].dt.date)

#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Header
st.sidebar.header("Das ist unsere Sidebar")

# Make a sidebar
#chart_language = st.sidebar.multiselect('Wie schätzt du deine Bildschirmzeit pro Tag ein?', 0, 10, 1)
chart_language = st.sidebar.multiselect('Select language', df['language'].unique().tolist())

# Show output of slider selection
st.sidebar.write("Die Tweets wurden aus verschiedenen Ländern gesendet. Welche Länder sind dabei und wir häufig wurde aus ihnen getweetet? Mit dem Land als einzige kategoriale Variable kann ein Donut-Diagramm die Verhältnisse gut darstellen.")

#-------------------
# HEADER

# Title of our app
st.title("Auswertung von russischen Trolltweets")
# Add header
st.header("Das ist die interaktive App von der Gruppe D")

#-------------------
# BODY

#-------------------
# Häufigste Länder
st.subheader("Häufigste Länder")
st.write("Here's my data:")

chart_region = alt.Chart(df.dropna()).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("count(region)", type="quantitative"),
    color=alt.Color("region", type="nominal", title='Länder'),
    tooltip=(
            alt.Tooltip("region")
    )
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

chart_language = alt.Chart(df.dropna()).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("count(language)", type="quantitative"),
    color=alt.Color("language", type="nominal", title='Sprachen'),
    tooltip=(
        alt.Tooltip("language")
    )
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

chart_followers = alt.Chart(df).mark_bar().encode(
  x=alt.X('author',
    title="Account-Name",
    sort="-y"
  ),
  y=alt.Y('max(followers)',
    title="Anzahl Follower"
  ),
  color=alt.Color("author",
    type="nominal",
    title='Account',
    legend=None),
  tooltip=(
        alt.Tooltip("max(followers)", title="Follower")
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

df['date'] = pd.to_datetime(df['publish_date'].dt.date)


chart_time = alt.Chart(df).mark_line().encode(
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

# Show plot
st.altair_chart(chart_time, use_container_width=True)


#-------------------
# Tweets nach Wochentag und Uhrzeit
st.subheader("Tweets nach Wochentag und Uhrzeit")
st.write("Here's my data:")

df['hour'] = df['publish_date'].dt.hour
df['weekday'] = df['publish_date'].dt.weekday

weekday_names = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
df['weekday_name'] = df['weekday'].replace(range(7), weekday_names)

heatmap = alt.Chart(df).mark_rect().encode(
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

