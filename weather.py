# weather
"""
run weather data retrieving scripts
"""
import requests


# Weather API Key (OpenWeatherMap)
weather_api_key = "75f6c15e22433ed3e7406b24691a0706"


class Weather:
    def __init__(self):
        pass

    # Function to get weather details
    def get_weather(self, city):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:
                weather_description = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                return f"The current weather in {city} is {weather_description} with a temperature of {temp}°C."
            else:
                return "I couldn't find the weather for that location. Please try another city."
        except Exception as e:
            print(f"Error fetching weather: {e}")
            return "Unable to get the weather right now."