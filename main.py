import streamlit as sl
import plotly.express as px
from functions import get_data


sl.title("WEATHER FORECAST")
place = sl.text_input("Place: ")
days = sl.slider("Forecast days: ", min_value=1 , max_value=5)
sbox = sl.selectbox("Select data to view: :", ("Temp","sky"))
sl.subheader(f"{sbox} for the next {days} days in {place}")

if place:
    filtered_data= get_data(place,days)

    if sbox == "Temp":
        temps = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x = dates,y = temps,labels={"x": "Date","y": "temp"})
        sl.plotly_chart(figure)
    if sbox == "sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain":
                "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]

        print(sky_conditions)
        sl.image(image_paths, width=100)

