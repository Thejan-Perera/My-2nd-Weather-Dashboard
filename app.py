import streamlit as st
import requests
import json



st.title("Thejan's Weather Dashboard")
st.header("Devolped by : Thejan Perera")
st.header("What is Weather GPT")
st.write("""Weather GPT is a weather application that tells you the weather of any location""")

latitude = st.sidebar.number_input("Enter the of the location",value = 0.00)
longitude = st.sidebar.number_input("Enter the longitude",value = 0.00)


api_url=f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,snow_depth,weather_code&timezone=auto'
resp = requests.get(api_url)
value = json.loads(resp.text)

teme = value['current']['temperature_2m']
humi = value['current']['relative_humidity_2m']
appa = value['current']['apparent_temperature']
isday = value['current']['is_day']
preci = value['current']['precipitation']
rain = value['current']['rain']
showers = value['current']['showers']
snowfall = value['current']['snowfall']
temp_cov_hou = value['current']['cloud_cover']


def day_or_night(is_day):
    if is_day == 1:
        return "Day"
    else:
        return "Night"


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Temperature_2m", teme)
with col2:
    st.metric("relative_humidity_2m'", humi)
with col3:
    st.metric("apparent_temperature", appa)
with col4:
    st.metric("is_day", day_or_night(isday))
with col5:
    st.metric("precipitation", preci)





