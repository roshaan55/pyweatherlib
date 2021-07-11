# pyweatherlib

Weather Library wich works on the weather api from **Open Weather Map** Website.

## Installation:
```nano
pip install pyweatherlib
```

## Usage:
```py
import WeatherModule as wm

try:
    city = input("Enter City: ")
    query = 'q=' + city
    w_data = wm.weather_data(query)
    wm.print_weather(w_data)
except:
    print('City name not found...')
```
For more examples see [Examples](https://github.com/roshaan55/pyweatherlib/blob/main/Examples "Examples of funcions of pyweatherlib").
