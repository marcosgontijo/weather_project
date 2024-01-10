import requests


def get_weather_data(cidade):
    API_KEY = "19f56434378efea1d316006c8ea5807d"

    # precisa receber a cidade que o usuario digitar para atribuir na api_url

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(api_url)

    requisicao_dic = requisicao.json()

    descricao = requisicao_dic['weather'][0]['description']

    temperatura_fahrenheit = requisicao_dic['main']['temp']  # formula °C = (°F - 32) × 5/9
    temperatura_celsius = (temperatura_fahrenheit - 273.15)

    return descricao, temperatura_celsius
