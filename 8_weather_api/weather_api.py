# the requests library allows you to send requests to APIs 
# APIs use HTTP protocol so the requests library sends HTTP requests
import requests

# to get the required info from the API, you need the website, API key, the city name, and the unit.
# using these three parameters, you can use requests.get()
# requests.get() returns the Response data type
# 
# the Response data type has: 
#   response.status_code (returns HTTP status of code, 200 is good, 404 is bad)
#   response.text (returns the content of the string as plain text)
#   response.json() (returns the data as a python dictionary)
#   response.headers (like the metadata of the info)
#   response.content

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather" # https://api.openweathermap.org/data/2.5/
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    # for params, the params are: q (location), appid (api key), and units
    response = requests.get(base_url, params=params)
    
    # data is now a dictionary of all the data
    if response.status_code == 200:
        # data contains: coord, weather, base, main, visibility, wind, clouds, dt, sys, timezone, id, name, cod
        # basically all the sub-categories
        data = response.json()
        
        # main contains: temp, feels_like, temp_min, temp_max, pressure, humidity, sea_level, grnd_level
        # basically all the main info
        main = data['main']

        # wind contains: speed, deg
        wind = data['wind']

        # this could be rewritten as 
        # weather = data['weather']
        # weather_state = weather[0]: IDK, maybe there are multiple weather states and 0 refers to the first? 
        # weather_description = weather['description']
        weather_description = data['weather'][0]['main']
        
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C, but feels like {main['feels_like']}°C.")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print(f"Error: Unable to fetch data for {city_name}")


if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "6f22d45461ea6663513d9f479a0317af"  # Replace with your actual API key
    get_weather(city, api_key)