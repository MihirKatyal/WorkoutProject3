import requests

def fetch_weather_data(api_key, city_name):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    Args:
        api_key (str): Your API key for the OpenWeatherMap API.
        city_name (str): Name of the city to fetch weather data for.
    Returns:
        dict: The weather data fetched from the API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    return response.json()
