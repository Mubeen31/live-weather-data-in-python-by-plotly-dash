import pandas as pd
from sqlalchemy import create_engine
import time


while True:
    time.sleep(6)
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df1 = df.tail(1)
    print(df1)
    MysqlConn = create_engine("mysql+pymysql://{user}:{password}@localhost/{db}".format(user = "root",
                                                                                        password = "sql_root_45t6",
                                                                                        db = "arduino_sensor_data"))
    df1.to_sql('datatable',
               con = MysqlConn,
               if_exists = 'append',
               chunksize = 1,
               index = False
               )

