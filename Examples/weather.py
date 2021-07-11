import pyweatherlib as pwl

try:
    city = input("Enter City: ")
    query = 'q=' + city
    w_data = pwl.weather_data(query)
    pwl.print_weather(w_data)
except:
    print('City name not found...')
