import pandas as pd
from sqlalchemy import create_engine
import time


while True:
    time.sleep(490)
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df1 = df.tail(1)
    print(df1)
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df2 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    df3 = df2.tail(1)
    MysqlConn = create_engine("mysql+pymysql://{user}:{password}@eu-cdbr-west-02.cleardb.net/{db}".
                              format(user = "b29440cf4f5695",
                                     password = "71632bff",
                                     db = "heroku_4e4427d7fc83901"))

    df1.to_sql('datatable',
               con = MysqlConn,
               if_exists = 'append',
               chunksize = 1,
               index = False
               )
    df3.to_sql('accuweather',
               con = MysqlConn,
               if_exists = 'append',
               chunksize = 1,
               index = False
               )
