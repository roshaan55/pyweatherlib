import WeatherModule as wm

try:
    city = input("Enter City: ")
    query = 'q=' + city
    w_data = wm.weather_data(query)
    wm.print_weather(w_data)
except:
    print('City name not found...')
