# pyweatherlib

Python Weather Library wich works on the weather api from **Open Weather Map** Website. It also includes the library to get the weather from google

## Installation:
```nano
pip install pyweatherlib
```

## Usage:
```py
import pyweatherlib as pwl

# Get your api key from # https://home.openweathermap.org/api_keys
api_key = '&APPID=' + 'YOUR API KEY HERE'
city = input("Enter City: ")
try:
    query = 'q=' + city
    w_data = weather_data(query, api_key)
    print("Today's {} Weather".format(city))
    print("Temperature: {}°C".format(pwl.temperature(w_data)))
    print("Feels Like {}°C".format(pwl.feels_like(w_data)))
    print("Wind Speed: {} m/s".format(pwl.wind_speed(w_data)))
    print("Humidity: {}%".format(pwl.humidity(w_data)))
    print("Pressure: {} hPa".format(pwl.pressure(w_data)))
    print("Description: {}".format(pwl.description(w_data)))
    print("Weather: {}".format(pwl.weather(w_data)))
except:
    if not pwl.internet():
        print("You're not connected to internet.")
    else:
        print('City name not found...')
```

## Google Weather Usage:

```py
from pyweatherlib.googleweather import *

try:
    x = datetime.now()
    # get data
    data = weather_data()
    # print data
    print("Weather for:", get_region(data))
    print("Date: {}".format(x.strftime("%d-%b-%Y")))
    print("Time: {}".format(x.strftime("%I:%M %p")))
    print(f"Temperature: {temperature(data)}°C")
    print("Description:", description(data))
    print("Precipitation:", precipitation(data))
    print("Humidity:", humidity(data))
    print("Wind:", wind(data))
    next_days_forecast(data)
except:
    print("You're not connected to internet.")
    
```

For more examples see [Examples](https://github.com/roshaan55/pyweatherlib/blob/main/Examples "Examples of funcions of pyweatherlib").
