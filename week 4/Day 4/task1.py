# Weather API client  

import requests

API_KEY = "e06b9dbdeb5f13f05cb3fcfc4e2c8899"  # Replace with your real API key
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    city_name = data['name']
    temperature = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    
    print(f"\nWeather in {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {weather_desc.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("City not found or API error.")
