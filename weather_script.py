import requests

def obtener_datos_meteorologicos(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return None

# Ejemplo de uso
ciudad = "Madrid"
api_key = "TU_API_KEY_AQUI"
datos = obtener_datos_meteorologicos(ciudad, api_key)
if datos:
    print(f"El clima en {ciudad}: {datos['weather'][0]['description']}")
    print(f"Temperatura: {datos['main']['temp']}°C")
else:
    print("No se pudieron obtener los datos meteorológicos.")