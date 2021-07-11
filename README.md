# pyweatherlib

Python Weather Library wich works on the weather api from **Open Weather Map** Website.

## Installation:
```nano
pip install pyweatherlib
```

## Usage:
```py
import pyweatherlib as pwl

try:
    city = input("Enter City: ")
    query = 'q=' + city
    w_data = pwl.weather_data(query)
    pwl.print_weather(w_data)
except:
    print('City name not found...')
```
For more examples see [Examples](https://github.com/roshaan55/pyweatherlib/blob/main/Examples "Examples of funcions of pyweatherlib").
