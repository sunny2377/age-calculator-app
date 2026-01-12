import streamlit as st
from datetime import date

st.set_page_config(page_title="Age Calulator", page_icon="🎂")
st.title("Age Calculator 🎂 !")
st.write("Enter your bithday below to find out exactly how old are you")

today = date.today()
birth_day = st.date_input("Enter your birthday", min_value = date(2000,1,1), max_value= today)
if birth_day:
    age_year =today.year - birth_day.year
    age_month = today.month - birth_day.month
    age_day = today.day - birth_day.day

    if age_day < 0:
        age_month -= 1
        age_day += 30

    if age_month < 0:
        age_year -= 1
        age_month += 12
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Years",value=age_year)

with col2:
    st.metric(label="Months", value= age_month)

with col3:
    st.metric(label= "Days", value= age_year)

totle_day = (today - birth_day).days
st.info(f"You have been on Earth for approximately **{totle_day}** days!")

