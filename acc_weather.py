import pandas as pd
from datetime import datetime, date, time
from requests_html import HTMLSession
import time

s = HTMLSession()


url = 'https://www.accuweather.com/en/gb/worcester/wr1-3/current-weather/331595'

while True:
    r = s.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

    acc_temp = r.html.find('div.display-temp', first = True).text

    left_string = r.html.find('div.left', first = True).text
    sp_stri_left = left_string.split()
    acc_wind_direction = sp_stri_left[1]
    acc_wind_speed = sp_stri_left[2]
    acc_humidity = sp_stri_left[9]
    acc_dew_point = sp_stri_left[17]

    right_string = r.html.find('div.right', first = True).text
    sp_stri_right = right_string.split()
    acc_pressure = sp_stri_right[2]

    dictionary_of_string = {'Temperature': [acc_temp], 'Wind Direction': [acc_wind_direction],
                            'Wind Speed': [acc_wind_speed], 'Humidity': [acc_humidity],
                             'Dew Point': [acc_dew_point], 'Atmospheric Pressure': [acc_pressure]}

    df1 = pd.DataFrame(dictionary_of_string)
    df1['Humidity'] = list(map(lambda x: x[:-1], df1['Humidity'].values))
    df1['Temperature'] = list(map(lambda x: x[:1], df1['Temperature'].values))
    df1['Dew Point'] = list(map(lambda x: x[:1], df1['Dew Point'].values))

    df1['Temperature'] = df1['Temperature'].astype(float)
    df1['Wind Direction'] = df1['Wind Direction'].astype(str)
    df1['Wind Speed'] = df1['Wind Speed'].astype(float)
    df1['Humidity'] = df1['Humidity'].astype(float)
    df1['Dew Point'] = df1['Dew Point'].astype(float)
    df1['Atmospheric Pressure'] = df1['Atmospheric Pressure'].astype(float)
    time.sleep(6)