#task3lesson33.py


"""
The Weather app

Write a console application which takes as an input a city name and returns current weather in the format of your choice. 
For the current task, you can choose any weather API or website or use openweathermap.org 
"""


import requests

# OpenWeatherMap API key
API_KEY = "430eec3054f6e79a2461b947e9d14567"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"  

def get_weather(city_name):
    """
    Fetches the current weather for a given city.
    """
    # Parameters for the API request
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        # Make the API request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        # Display the weather information
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather data: {e}")
    except KeyError:
        print("City not found. Please check the city name and try again.")

def main():
    """
    Main function to run the console application.
    """
    print("Welcome to the Weather App!")
    city_name = input("Enter the city name: ").strip()
    if city_name:
        get_weather(city_name)
    else:
        print("City name cannot be empty.")

if __name__ == "__main__":
    main()

