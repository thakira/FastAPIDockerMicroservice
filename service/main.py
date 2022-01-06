from fastapi import FastAPI, Request
import uvicorn
from random import randrange
import weather_data
from fastapi.templating import Jinja2Templates


#from models.weather_model import WeatherModel

app = FastAPI()
templates = Jinja2Templates(directory="html")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/number')
def random_number(request: Request):
    return templates.TemplateResponse("number.html", {"request": request, "number": str(randrange(0,100,2))})



@app.get('/weather/{city}')
async def weather_search(request: Request, city: str):
    weather = await weather_data.get_weather(city)
    if not weather:
        raise fastapi.HTTPException(status_code=404)

    tempc = str(int(weather['main']['temp'] - 273.15))
    print(tempc + ", " + city + ", " +  weather['name'] + ", " +  weather['weather'][0]['main'])
    return templates.TemplateResponse("weather.html", {"request": request, "city": city, "weather_city": weather['name'], "weather_tempc": tempc, "weather_description":(weather['weather'][0]['main']).lower()})
    # return """
    #    <html>
    #        <head>
    #        </head>
    #        <body>
    #            <h1>Weather in {city} </h1>
    #            <p>The Weather in {weather['name']}:</p>
    #            <p>The temperature is {str(tempc)} degrees Celsius and it is/there are {(weather['weather'][0]['main']).lower()}.</p>
    #        </body>
    #    </html>
    #    """
    # html = "<html><p>The Weather in " + weather['name'] + ":\nThe temperature is " + str(tempc) + \
    #        " degrees Celsius and it is/there are " + (weather['weather'][0]['main']).lower() + ".</p></html>"
    # return html

if __name__ == '__main__':
    uvicorn.run(app)