from weather_api import fetch_weather_data
from file_io import write_data_to_file, read_data_from_file
from visual import generate_temperature_graph

def main():
    API_KEY = 'your_api_key_here'  # Replace with your actual OpenWeatherMap API key
    CITY_NAME = 'London'  # Replace with your preferred city

    # Fetch and write weather data
    weather_data = fetch_weather_data(API_KEY, CITY_NAME)
    write_data_to_file(weather_data, 'weather_data.json')

    # Read the weather data from file
    read_weather_data = read_data_from_file('weather_data.json')

    # Assuming weather_data is a list of weather reports; if not, adjust accordingly
    # Here you might need to convert the single data point to a list for the graph generation
    generate_temperature_graph([read_weather_data], CITY_NAME)

if __name__ == "__main__":
    main()
