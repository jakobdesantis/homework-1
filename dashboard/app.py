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
df = pd.read_csv('../data/external/data.csv')

# Data transformation
df['Date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
#-----------
df2 = df.drop(labels=range(5000, 250000), axis=0)
#-----------
df2["length"] = df2["content"].str.len()
#----------
df2['publish_date']= pd.to_datetime(df2['publish_date']).dt.date
df2['publish_date'] = pd.to_datetime(df2['publish_date'])
#-----------




#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Make a chart_language
chart_language = st.sidebar.multiselect('Wie schätzt du deine Bildschirmzeit pro Tag ein?', 0, 10, 1)

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
# Verteilung der Sprachen
st.subheader("Verteilung der Sprachen")
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
    sort='-y',
    title="Account-Name"
  ),
  y=alt.Y('count(region)',
    title="Anzahl Follower"
  )
).properties(
    title='Accounts mit den meisten Followern',
    width=800,
    height=300
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
# Zusammenhang Tweetlänge und Anzahl Follower
st.subheader("Zusammenhang Tweetlänge und Anzahl Follower")
st.write("Here's my data:")

source = df2

chart_length = alt.Chart(source).mark_point().encode(
    x=alt.X('length',
        title="Tweet-Länge (Zeichen)"
    ),
    y=alt.Y('followers',
        title="Anzahl der Follower des postenden Accoutns"
    )
).properties(
    title='Anzahl der Follower im Zusammenhang mit der Tweet-Länge',
    width=800,
    height=300
)

chart_length.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)
c= chart_length

# Show plot
st.altair_chart(c, use_container_width=True)


#-------------------
# Posts je nach Zeit
st.subheader("Posts je nach Zeit")
st.write("Here's my data:")

source = df2

chart_time = alt.Chart(source).mark_line().encode(
    x=alt.X("publish_date",
        title="Datum"
    ),
    y=alt.Y("count(publish_date)",
        title="Anzahl der Tweets"
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


