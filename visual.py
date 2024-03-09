import matplotlib.pyplot as plt

def generate_temperature_graph(data, city_name):
    temperatures = [data_point['main']['temp'] for data_point in data]
    dates = [data_point['dt'] for data_point in data]  

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o')
    plt.title(f'Temperature Trend for {city_name}')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (K)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
