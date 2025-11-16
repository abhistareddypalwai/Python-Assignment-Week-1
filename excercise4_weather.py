# Exercise 4: Weather Data Fetcher & Analyzer
# Introduction:
# This program uses the OpenWeatherMap API to fetch real-time weather data for a given city,
# analyze the temperature, wind, and humidity, and then log the results into a CSV file.


import requests  # Used to send HTTP requests to the OpenWeatherMap API
import csv       # Used to write weather data into a CSV file
from datetime import datetime  # Used to add timestamp to the logged data




def fetch_weather(city: str, api_key: str) -> dict:
    
    # Base URL for OpenWeatherMap Current Weather API (metric = Celsius)
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters to send with the GET request
    params = {
        "q": city,        # City name
        "appid": api_key, # Your API key
        "units": "metric" # Temperature in Celsius
    }

    try:
        # Send GET request to the API with the parameters
        response = requests.get(base_url, params=params)
        
        # If status code is not 200, raise an HTTPError
        response.raise_for_status()
        
        # Convert the response JSON string into a Python dictionary
        data = response.json()
        
        # Return the dictionary
        return data
    
    except requests.exceptions.HTTPError as http_err:
        # Print HTTP-specific error (like 404, 401, etc.)
        print(f"HTTP error occurred: {http_err}")
        return {}
    except requests.exceptions.RequestException as req_err:
        # Print general network errors (like connection problems)
        print(f"Network error occurred: {req_err}")
        return {}
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return {}


def analyze_weather(weather_data: dict) -> str:

       # If the dictionary is empty or missing 'main', return an error message
    if not weather_data or "main" not in weather_data:
        return "Weather data is not available or invalid."

    # Extract main temperature from the 'main' field
    temp = weather_data["main"]["temp"]           # Temperature in °C
    # Extract wind speed if available, otherwise set to 0
    wind_speed = weather_data.get("wind", {}).get("speed", 0)  # Wind speed in m/s
    # Extract humidity from 'main'
    humidity = weather_data["main"]["humidity"]   # Humidity percentage

    # Start building the summary based on temperature range
    if temp <= 10:
        summary = "Cold (≤10°C)"
    elif 11 <= temp <= 24:
        summary = "Mild (11-24°C)"
    else:
        summary = "Hot (≥25°C)"

    # Add warnings based on wind speed and humidity
    warnings = []

    # Check if wind speed is greater than 10 m/s
    if wind_speed > 10:
        warnings.append("High wind alert!")
    
    # Check if humidity is greater than 80%
    if humidity > 80:
        warnings.append("Humid conditions!")

    # Join warnings into a single string if any exist
    if warnings:
        summary += " | Warnings: " + ", ".join(warnings)

    # Return the final summary string
    return summary


def log_weather(city: str, filename: str, api_key: str):
    
    # Fetch weather data using the fetch_weather function
    weather_data = fetch_weather(city, api_key)

    # If fetch failed, stop the function
    if not weather_data or "main" not in weather_data:
        print("Could not log weather because data is invalid.")
        return

    # Analyze weather to get a summary string
    summary = analyze_weather(weather_data)

    # Extract needed fields safely with .get()
    temp = weather_data["main"]["temp"]                     # Current temperature
    feels_like = weather_data["main"].get("feels_like", "") # Feels-like temperature
    humidity = weather_data["main"]["humidity"]             # Humidity percentage
    wind_speed = weather_data.get("wind", {}).get("speed", "")  # Wind speed
    description = weather_data["weather"][0]["description"] # Short weather description
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")# Current date and time

    # Open the CSV file in append mode ('a') and create it if it doesn't exist
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)  # Create a CSV writer object

        # Optionally: write header if file is new (simple check could be added later)
        # For now, assume you know the columns and write them once manually if needed.

        # Write one row with the city weather data
        writer.writerow([
            timestamp,   # Date and time of logging
            city,        # City name
            temp,        # Temperature
            feels_like,  # Feels-like temperature
            humidity,    # Humidity
            wind_speed,  # Wind speed
            description, # Weather description
            summary      # Our analysis summary
        ])

    # Print confirmation message
    print(f"Weather for {city} has been logged to {filename}.")


if __name__ == "__main__":
    # Ask the user to input the API key (or you can paste directly for testing)
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    # Ask the user to input the city name
    city_name = input("Enter city name: ")
    
    # Fetch weather data for the given city
    data = fetch_weather(city_name, api_key)
    
    # Print the raw data (optional, for debugging)
    # print(data)
    
    # Analyze the fetched weather data
    summary_text = analyze_weather(data)
    
    # Print the summary analysis
    print("Weather summary:", summary_text)
    
    # Log weather into a CSV file named 'weather_log.csv'
    log_weather(city_name, "weather_log.csv", api_key)

    # Conclusion comment for the exercise
    # Conclusion:
    # This exercise demonstrated how to connect to a live weather API,
    # process JSON data, classify weather conditions, and store the
    # results in a CSV file for future analysis.


