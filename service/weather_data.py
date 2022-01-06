import httpx
from typing import Optional
#from models.weather_model import WeatherModel


#async def get_weather(city_subtext: str) -> Optional[WeatherModel]:
async def get_weather(city_subtext: str):
    print("City:" + city_subtext)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_subtext},&APPID=03bddb34221748fa023596b3388b54e6'

    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()

        print(resp, resp.text)
        data = resp.json()

    results = data['weather']
    if not results:
        return None

    #weather = WeatherModel(results[0])
    weather = (data)
    return weather
