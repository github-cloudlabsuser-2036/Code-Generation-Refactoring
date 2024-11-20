import requests

def get_weather(city, country, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},{country}',
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    city = input("Ingrese la ciudad: ")
    country = input("Ingrese el país: ")
    api_key = 'a7bfff3726ad74eba9ad5385ed814e10'  # Reemplaza con tu clave de API de OpenWeatherMap

    weather_data = get_weather(city, country, api_key)
    if weather_data:
        print(f"Clima en {city}, {country}:")
        print(f"Temperatura: {weather_data['main']['temp']}°C")
        print(f"Descripción: {weather_data['weather'][0]['description']}")
    else:
        print("No se pudo obtener la información del clima.")

if __name__ == "__main__":
    main()