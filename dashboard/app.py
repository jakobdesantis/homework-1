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
#df2 = df


# Data transformation

#Löschen nicht benötigter Spalten
df.drop(df.columns[[0, 1, 2, 3, 5, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]], axis=1, inplace=True)

#Spalte "publish_date" in das "datetime"-Format umwandeln
df['publish_date'] = pd.to_datetime(df['publish_date'], format='%m/%d/%Y %H:%M')

#Spalte "date" hinzufügen, die nur das Datum, aber nicht die Uhrzeit enthält
df['date'] = pd.to_datetime(df['publish_date'].dt.date)

#Spalte "hour" hinzufügen, die nur die Stunde enthält
df['hour'] = df['publish_date'].dt.hour

#Spalte "weekday" hinzufügen, die den Wochentag enthält
df['weekday'] = df['publish_date'].dt.weekday

#Spalte "weekday_name" hinzufügen, die den Namen des Wochentags enthält
weekday_names = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
df['weekday_name'] = df['weekday'].replace(range(7), weekday_names)

#-------------------
# START OF APP

#-------------------
# SIDEBAR

# Header
st.sidebar.header("Ihre Erfahrung mit Troll-Tweets")

# Make a sidebar
chart_followers = st.sidebar.multiselect('Welche dieser Accounts kennen Sie bereits?:', df['author'].unique().tolist())

# Show output of slider selection
st.sidebar.write("Von den Troll-Tweet-Accounts, mit den meisten Follower, kenne ich", chart_followers)

#-------------------
# HEADER
st.write("Gruppe D")

# Title of our app
st.title("Auswertung russischer Troll-Tweets")
# Add header
st.write("Unsere interaktive App wertet russische Troll-Tweets, nach Länder, Sprachen, Follower, Datum und Region sowie Wochentag und Uhrzeit, aus.")
st.write("Der Datensatz enthält knapp 3 Millionen russische Troll-Tweets, die zwischen Februar 2012 und Mai 2018 veröffentlicht wurden. Da der ursprüngliche Datensatz sehr umfangreich ist, wird im Folgenden nur ein Ausschnitt von knapp 5.000 Tweets analysiert.")

#-------------------
# BODY

#-------------------
# Häufigste Länder
st.subheader("Länder mit den meist gesendeten Tweets")
st.write("Die Tweets wurden aus verschiedenen Ländern gesendet.")
st.write("Welche Länder sind dabei und wie häufig wurde aus ihnen getweetet?")
st.write("Mit dem Land als einzige kategoriale Variable kann ein Donut-Diagramm die Verhältnisse gut darstellen.")

chart_region = alt.Chart(df.dropna()).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("count(region)", type="quantitative"),
    color=alt.Color("region", type="nominal", title='Länder'),
    tooltip=(alt.Tooltip("region"))
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

# Show plot
st.altair_chart(chart_region, use_container_width=True)


#-------------------
# Häufigste Sprachen
st.subheader("Tweets mit den häufigsten Sprachen")
st.write("Welche Sprachen sind besonders stark vertreten?")
st.write("Hier ist die einzige kategoriale Variable die Sprache. Erneut haben wir uns für ein Donut-Diagramm entschieden.")

chart_language = alt.Chart(df.dropna()).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("count(language)", type="quantitative"),
    color=alt.Color("language", type="nominal", title='Sprachen'),
    tooltip=(alt.Tooltip("language"))
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

# Show plot
st.altair_chart(chart_language, use_container_width=True)


#-------------------
# Follower-Verteilung
st.subheader("Follower-Verteilung")
st.write("Wie groß ist das Publikum der Troll-Accounts?")
st.write("Gibt es Accounts mit besonders vielen Follower?")
st.write("Die Anzahl der Follower ist eine einzige numerische Variable, die wir diesmal als Balkendiagramm darstellen.")

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
  tooltip=(alt.Tooltip("max(followers)", title="Follower"))
).properties(
    title='Accounts mit den meisten Follower',
    width=800,
    height=300,
)

chart_followers.configure_title(
    fontSize=16,
    font='Arial',
    color='black',
    anchor='middle'
)

# Show plot
st.altair_chart(chart_followers, use_container_width=True)


#-------------------
# Posts nach Datum und Region
st.subheader("Posts nach Datum und Region")
st.write("Gibt es Zeiträume, in denen die Troll-Konten besonders aktiv waren?")
st.write("Diese Frage lässt sich mit der Anzahl der Tweets pro Tag erkennen.")
st.write("Beim Datum und der Anzahl der Tweets pro Tag handelt sich um zwei numerische Variablen.")
st.write("Diese Auswertung veranschaulichen wir im Folgenden als Liniendiagramm.")
st.write("Die Anzahl der Posts soll im Intervall von je einem Tag angezeigt werden:")

df['date'] = pd.to_datetime(df['publish_date'].dt.date)

chart_time = alt.Chart(df.dropna()).mark_line().encode(
    x=alt.X("date", title="Datum"),
    y=alt.Y("count(date)", title="Anzahl der Tweets"),
    color=alt.Color("region", title="Region"),
    tooltip=alt.Tooltip("count(date)", title="Anzahl der Tweets")
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
st.subheader("Posts nach Wochentag und Uhrzeit")
st.write("Zu welchen Wochentagen und Uhrzeiten waren die Konten besonders aktiv?")
st.write("Dazu benötigen wir drei Werte: Den Wochentag, die Uhrzeit (Einheit: Stunde) und die Anzahl der Tweets pro Wochentag und Uhrzeit.")
st.write("Die Anzahl der Tweets und die Uhrzeit sind numerische Variablen, der Wochentag ist jedoch eine kategoriale Variable.")
st.write("Diese Kombination stellen wir in einer Heatmap dar.")
st.write("Dafür werden zuerst zwei weitere Spalten „hour“ und „weekday“ erstellt.")

region_select = alt.binding_select(options=df["region"].dropna().unique())
region_select_widget = alt.selection_single(bind=region_select, name="Region")

heatmap = alt.Chart(df.dropna()).mark_rect().encode(
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
    tooltip = alt.Tooltip("count(weekday_name)", title="Anzahl der Tweets")
).add_selection(
    region_select_widget
).transform_filter(
    region_select_widget
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

# Show plot
st.altair_chart(heatmap, use_container_width=True)