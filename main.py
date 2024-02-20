import datetime
import streamlit as sl
import plotly.express as px
from functions import get_data

# placeholder for images
images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain":
                "images/rain.png", "Snow": "images/snow.png"}

# UI components for display
sl.title("WEATHER FORECAST")
place = sl.text_input("Place: ")
days = sl.slider("Forecast days: ", min_value=1, max_value=5)
sbox = sl.selectbox("Select data to view: :", ("Temp", "sky"))
sl.subheader(f"{sbox} for the next {days} days in {place}")

# If the input box contains text
if place:
    try:
        # Location input and amount of days
        filtered_data = get_data(place, days)
        # If user requesting just the temperature
        if sbox == "Temp":
            temps = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": "temp"})
            sl.plotly_chart(figure)
            # Section for displaying textual weather forecast
            sl.subheader("Weather Forecast")
            for day_data in filtered_data:
                # Converting date string to datetime object
                date_obj = datetime.datetime.strptime(day_data['dt_txt'], "%Y-%m-%d %H:%M:%S")
                # Get the day of the week
                day_of_week = date_obj.strftime("%A")
                # Displaying textual weather forecast
                sl.write("---")
                sl.write(f"**{day_of_week}**")
                sl.write(f"**Temperature:** {day_data['main']['temp']}°C")
                sl.write(f"**Weather:** {day_data['weather'][0]['description']}")
                # Adding sky images
                weather_condition = day_data['weather'][0]['main']
                if weather_condition in images:
                    sl.image(images[weather_condition], width=100)
        # If user requesting sky condition with images
        if sbox == "sky":
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            dates = [dict["dt_txt"] for dict in filtered_data]

            print(sky_conditions)
            # Displayed image properties
            sl.image(image_paths, dates, width=100)
    # If location/city not found
    except KeyError:
        sl.write("Type in a correct City")
