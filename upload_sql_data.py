import pandas as pd
from sqlalchemy import create_engine
import time
import MySQLdb as mysql


while True:
    time.sleep(6)
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df1 = df.tail(1)
    print(df1)
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df2 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    df3 = df2.tail(1)
    # MysqlConn = create_engine("mysql+pymysql://{user}:{password}@eu-cdbr-west-02.cleardb.net/{db}".format(user = "b54eb1e6af434b",
    #                                                                                     password = "181636f95f46e13",
    #                                                                                     db = "heroku_323e0ab91ec4d38"))
    # MysqlConn = create_engine(
    #     "mysql+pymysql://{user}:{password}@127.0.0.1/{db}".format(user = "root",
    #                                                                                 password = "sql_root_45t6",
    #                                                                                 db = "arduino_sensor_data"))
    # df1.to_sql('datatable',
    #            con = MysqlConn,
    #            if_exists = 'append',
    #            chunksize = 1,
    #            index = False
    #            )
    # df3.to_sql('accuweather',
    #            con = MysqlConn,
    #            if_exists = 'append',
    #            chunksize = 1,
    #            index = False
    #            )

    # conn = mysql.connect(host = 'eu-cdbr-west-02.cleardb.net',
    #                      database = 'heroku_323e0ab91ec4d38',
    #                      user = 'b54eb1e6af434b',
    #                      password = '181636f95f46e13')
    #
    # cursor = conn.cursor()
    #
    # cursor.execute('DROP TABLE IF EXISTS datatable;')
    #
    # cursor.execute('CREATE TABLE datatable (Date Time DATETIME, '
    #                'Humidity FLOAT, '
    #                'Rain FLOAT, '
    #                'Photo Resistor Value FLOAT, '
    #                'Photo Resistor LED TEXT, '
    #                'Revolution FLOAT, '
    #                'RPM FLOAT, '
    #                'Wind Speed KPH FLOAT, '
    #                'Wind Degree FLOAT, '
    #                'Wind Direction TEXT, '
    #                'CO2 Level FLOAT, '
    #                'Temperature FLOAT, '
    #                'Air Pressure FLOAT)'
    #                )
    # for row in df1.itertuples():  # itertuples() function is used to iterate tuple rows
    #     cursor.execute('''
    #                 INSERT INTO datatable (Date Time, Humidity, Rain, Photo Resistor Value,
    #                                        Photo Resistor LED, Revolution, RPM, Wind Speed KPH,
    #                                        Wind Degree, Wind Direction, CO2 Level, Temperature,
    #                                        Air Pressure)
    #                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    #                 ''',
    #                    (row[0],
    #                     row[1],
    #                     row[2],
    #                     row[3],
    #                     row[4],
    #                     row[5],
    #                     row[6],
    #                     row[7],
    #                     row[8],
    #                     row[9],
    #                     row[10],
    #                     row[11],
    #                     row[12]
    #                     ))
    #
    #     conn.commit()

