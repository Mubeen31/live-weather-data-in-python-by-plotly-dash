import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime, date, time
import numpy as np
from datetime import datetime, date, time
from sklearn import linear_model
import sqlalchemy
from dash import dash_table as dt
import time

# engine = sqlalchemy.create_engine(
#         'mysql+pymysql://b54eb1e6af434b:181636f95f46e13@eu-cdbr-west-02.cleardb.net:3306/heroku_323e0ab91ec4d38')
# df = pd.read_sql_table('accuweather', engine)
# df1 = df.tail(1)
# print(df1)

header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
               'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
df5 = pd.read_csv('weather_data.csv', names = header_list)
df6 = df5.tail(2)

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server = app.server
app.title = "Weather Sensor Data"

app.layout = html.Div([
    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 6000,
                     n_intervals = 0),
    ]),

    html.Div([
        dcc.Interval(id = 'update_time',
                     interval = 1000,
                     n_intervals = 0),
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.I(className = "fas fa-home"),
                    ], className = 'title_image'),
                    html.H6('Newtown Road, Worcester, England',
                            style = {'color': 'white'},
                            className = 'title'
                            ),
                ], className = 'logo_title'),
                html.Div(id = 'title_image_value')
            ], className = 'title_image_value_row'),
            html.A(href = 'https://www.accuweather.com/en/gb/worcester/wr1-3/current-weather/331595',
                   target = '_blank',
                   children = [html.P('AccuWeather Data: Worcester, Worcestershire, England', className = 'link')]),
        ], className = 'title_date_time_container')
    ], className = 'title_date_time_container_overlay'),

    html.Div([
        html.Div([

            html.Div(id = 'background_image_container',
                     className = 'background_image'),

            html.Div([
                html.Div([

                    html.Div([
                        html.Div([
                            html.Div(id = 'time_value')
                        ], className = 'current_weather_time_value'),
                        html.Div([
                            html.Div([
                                html.Div(id = 'forecast_text')
                            ], className = 'current_weather_time_value'),
                            html.Div([
                                html.Div([
                                    html.Div(id = 'forecast_image')
                                ], className = 'current_weather_time_value'),
                                html.Div([
                                    html.Div(id = 'forecast_value')
                                ], className = 'current_weather_time_value'),
                            ], className = 'forecast_image_value_row'),
                            html.Div([
                                html.Div(id = 'forecast_time')
                            ], className = 'current_weather_time_value'),
                        ], className = 'forecast_column')
                    ], className = 'current_weather_time_value_forecast_row'),

                    html.Div([
                        html.Div(id = 'status_temperature',
                                 className = 'status_temperature_value'),
                    ], className = 'status_temperature_value_row'),

                    html.Div([
                        html.Div(id = 'first_sentence',
                                 className = 'status_paragraph_value'),
                        html.Div(id = 'second_sentence',
                                 className = 'status_paragraph_value'),
                        html.Div(id = 'third_sentence',
                                 className = 'status_paragraph_value'),
                    ], className = 'sentence_row'),

                    html.Div([
                        html.Div(id = 'numeric_value',
                                 className = 'status_numeric_value'),
                    ], className = 'status_numeric_value_row')

                ], className = 'background_image_current_weather_time_column'),
            ], className = 'background_image_current_weather_time_content_row')

        ], className = 'background_image_current_weather_time_column'),

        html.Div([
            html.Div([
                html.P('AccuWeather Data', className = 'acc_data_text'),
                html.Div([
                    html.Div(id = 'accu_temp'),
                    html.Div(id = 'accu_hum'),
                ], className = 'accu_temp_hum_row'),
                html.Hr(className = 'acc_bottom_border'),
                html.Div([
                    html.Div(id = 'accu_dew_point'),
                    html.Div(id = 'accu_atm_pressure'),
                ], className = 'accu_temp_hum_row'),
                html.Hr(className = 'acc_bottom_border'),
                html.Div([
                    html.Div(id = 'accu_wind_speed'),
                    html.Div(id = 'accu_wind_direction'),
                ], className = 'accu_temp_hum_row'),
            ], className = 'accu_column')
        ], className = 'accu_weather_card_background_color'),
    ], className = 'accu_weather_card_background_color_row'),

    html.Div([
        html.P('More Details',
               className = 'more_details'),
        html.Div(className = 'more_details_bottom_border'),
    ], className = 'background_color_more_details'),

    html.Div([

        html.Div([
            html.Div([
                html.Div([
                    html.Div(id = 'air_pressure',
                             className = 'air_pressure_value'),
                    html.Div(id = 'air_quality',
                             className = 'air_quality_value'),
                ], className = 'atmospheric_pressure_quality_value_column'),
                html.Div([
                    html.Div(id = 'sun_rise_status'),
                    html.Img(src = app.get_asset_url('climate.png'),
                             className = 'circle_image'),
                    html.Div(id = 'sun_set_status'),
                ], className = 'sun_rise_set_status_value'),
            ], className = 'atmospheric_pressure_quality_value_sun_row'),
        ], className = 'background_color_more_details_card1'),

        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id = 'wind_speed',
                              animate = False,
                              config = {'displayModeBar': False},
                              className = 'wind_speed_graph'),
                    html.Div(id = 'wind_speed_value',
                             className = 'wind_speed_numeric_value')
                ], className = 'wind_speed_numeric_value_column'),

                html.Div(id = 'wind_direction_value',
                         className = 'wind_speed_direction_numeric_value'),
            ], className = 'wind_speed_direction_numeric_value_row')
        ], className = 'background_color_more_details_card2'),

    ], className = 'content_row'),



# dt.DataTable(id = 'my_datatable',
#              columns = [{'name': i, 'id': i} for i in
#                         df5.loc[:, ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
#                                     'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']]],
#              data=df6.to_dict('records'),
#              # page_action='native',
#              # page_size=20,
#              # editable=False,
#              sort_action = "native",
#              sort_mode = "multi",
#              # column_selectable="single",
#              # fill_width=False,
#              style_table={'minWidth': '100%',
#                           'maxWidth': '100%',
#                           'margin': '0 auto',
#                           'margin-top': '20px',
#                           # 'margin-left': '50px',
#                           # 'margin-right': '50px'
#                           },
#              virtualization = True,
#              style_cell = {'textAlign': 'left',
#                            'min-width': '100px',
#                            'backgroundColor': '#1f2c56',
#                            'color': '#FEFEFE',
#                            'border-bottom': '0.01rem solid #19AAE1'
#                            },
#              style_as_list_view = True,
#              style_header = {'backgroundColor': '#1f2c56',
#                              'fontWeight': 'bold',
#                              'font': 'Lato, sans-serif',
#                              'color': 'orange',
#                              'border': '#1f2c56'
#                              },
#              style_data = {'textOverflow': 'hidden', 'color': 'white'},
#              fixed_rows = {'headers': True},
#              )
])


@app.callback(Output('title_image_value', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100

    if get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('night-rain.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]

    if get_rain_value >= 800.0 and get_rain_value <= 900.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('rain.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]

    if get_rain_value < 800.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('rain.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]

    if get_photo_resistor_value < 300.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('moon.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]

    if get_photo_resistor_value < 300.0 and convert_pa_to_mb >= 1000.00 and convert_pa_to_mb < 1002.00:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('fog-moon.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]

    elif get_photo_resistor_value >= 300.0 and get_photo_resistor_value <= 800.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('cloud.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]

    elif get_photo_resistor_value > 800.0 and get_photo_resistor_value <= 900.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('partly-cloud.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]

    elif get_photo_resistor_value > 900.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunny.png'),
                         className = 'cloud_image'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'temperature_value'
                       ),
            ], className = 'image_value'),
        ]


@app.callback(Output('background_image_container', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]

    if get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.Div(style = {'background-image': 'url("/assets/night-rain.jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'background_image_container'),
        ]

    if get_rain_value >= 800.0 and get_rain_value <= 900.0:
        return [
            html.Div(style = {'background-image': 'url("/assets/rain.jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'background_image_container'),
        ]
    if get_rain_value < 800.0:
        return [
            html.Div(style = {'background-image': 'url("/assets/rain.jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'background_image_container'),
        ]

    elif get_photo_resistor_value < 300.0:
        return [
            html.Div(style = {'background-image': 'url("/assets/night.jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'background_image_container'),
        ]

    elif get_photo_resistor_value >= 300.0 and get_photo_resistor_value <= 800.0:
        return [
            html.Div(style = {'background-image': 'url("/assets/cloudy-day.jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'background_image_container'),
        ]
    elif get_photo_resistor_value > 800.0 and get_photo_resistor_value <= 900.0:
        return [
            html.Div(style = {'background-image': 'url("/assets/partly-cloudy.jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'background_image_container'),
        ]
    elif get_photo_resistor_value > 900.0:
        return [
            html.Div(style = {'background-image': 'url("/assets/sunny.jpg")',
                              'background-repeat': 'no-repeat',
                              'background-size': 'auto'
                              },
                     className = 'background_image_container'),
        ]


@app.callback(Output('accu_temp', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_temp = df1['Temperature'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0]
    difference_data = get_temp - acc_temp

    if get_temp == acc_temp:
        return [
            html.Div([
                html.P('Temperature', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_temp), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif difference_data >= 0.01 and difference_data <= 0.49:
        return [
            html.Div([
                html.P('Temperature', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_temp), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif difference_data <= -0.01 and difference_data >= -0.50:
        return [
            html.Div([
                html.P('Temperature', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_temp), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif get_temp != acc_temp:
        return [
            html.Div([
                html.P('Temperature', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_temp), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]


@app.callback(Output('accu_hum', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_hum = df1['Humidity'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_hum = df['Humidity'].tail(1).iloc[0]

    if get_hum == acc_hum:
        return [
            html.Div([
                html.P('Humidity', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.0f}%'.format(acc_hum), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif get_hum != acc_hum:
        return [
            html.Div([
                html.P('Humidity', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.0f}%'.format(acc_hum), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]


@app.callback(Output('accu_dew_point', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_dew_point = df1['Dew Point'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_humidity = df['Humidity'].tail(1).iloc[0].astype(float)
    dew_point = get_temp - ((100 - get_humidity) / 5)
    difference_data = dew_point - acc_dew_point

    if dew_point == acc_dew_point:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif difference_data >= 0.01 and difference_data <= 0.49:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif difference_data <= -0.01 and difference_data >= -0.50:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif dew_point != acc_dew_point:
        return [
            html.Div([
                html.P('Dew Point', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}°C'.format(acc_dew_point), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]


@app.callback(Output('accu_atm_pressure', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_atm_pressure = df1['Atmospheric Pressure'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_atm_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)

    if get_atm_pressure == acc_atm_pressure:
        return [
            html.Div([
                html.P('Atmospheric Pressure', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}'.format(acc_atm_pressure), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif get_atm_pressure != acc_atm_pressure:
        return [
            html.Div([
                html.P('Atmospheric Pressure', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f}'.format(acc_atm_pressure), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]


@app.callback(Output('accu_wind_speed', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_wind_speed = df1['Wind Speed'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)

    if get_wind_speed == acc_wind_speed:
        return [
            html.Div([
                html.P('Wind Speed', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f} kph'.format(acc_wind_speed), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif get_wind_speed != acc_wind_speed:
        return [
            html.Div([
                html.P('Wind Speed', className = 'acc_text'),
                html.Div([
                    html.P('{0:,.2f} kph'.format(acc_wind_speed), className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]


@app.callback(Output('accu_wind_direction', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    acc_header_list = ['Temperature', 'Wind Direction', 'Wind Speed', 'Humidity', 'Dew Point', 'Atmospheric Pressure']
    df1 = pd.read_csv('acc_weather_data.csv', names = acc_header_list)
    acc_wind_direction = df1['Wind Direction'].tail(1).iloc[0]
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)

    # degree_value = [112.5, 67.5, 90, 157.5, 135, 202.5, 180, 22.5, 45, 247.5, 225, 337.5, 0, 292.5, 315, 270]
    # direction_value = ["ESE", "ENE", "E", "SSE", "SE", "SSW", "S", "NNE", "NE", "WSW", "SW", "NNW", "N", "WNW", "NW",
    #                    "W"]
    # dictionary_degree_direction = {'Degree': degree_value, 'Direction': direction_value}
    # df2 = pd.DataFrame(dictionary_degree_direction)
    # df2['Degree'] = df2['Degree'].astype(float)
    # df2['Direction'] = df2['Direction'].astype(str)
    # merge_df = pd.merge(left = df,
    #                     right = df2,
    #                     how = 'inner',
    #                     left_on = ['Wind Direction'],
    #                     right_on = ['Degree'])

    get_wind_direction = df['Wind Direction'].tail(1).iloc[0]


    if get_wind_direction == acc_wind_direction:
        return [
            html.Div([
                html.P('Wind Direction', className = 'acc_text'),
                html.Div([
                    html.P(acc_wind_direction, className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-check-circle fa-lg"),
                    ], className = 'acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]
    elif get_wind_direction != acc_wind_direction:
        return [
            html.Div([
                html.P('Wind Direction', className = 'acc_text'),
                html.Div([
                    html.P(acc_wind_direction, className = 'acc_value'),
                    html.Div([
                        html.I(className = "far fa-times-circle fa-lg"),
                    ], className = 'not_equal_acc_image'),
                ], className = 'acc_value_image_row')
            ], className = 'acc_value_image_column'),
        ]


@app.callback(Output('time_value', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')

    return [
        html.Div([
            html.Div([
                html.P('CURRENT WEATHER'),
            ], className = 'current_weather'),
            html.P(time,
                   className = 'current_time'
                   ),
        ], className = 'current_weather_time'),
    ]


@app.callback(Output('forecast_text', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')

    return [
            html.Div([
                html.P('FORECAST'),
            ], className = 'current_weather'),
    ]


@app.callback(Output('forecast_image', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')

    return [
        html.Img(src = app.get_asset_url('rain.png'),
                 className = 'forecast_image'),
    ]


@app.callback(Output('forecast_value', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df2 = df[['Humidity', 'Temperature']].tail(100)
    df_x = df2.drop(['Temperature'], axis = 1)
    df_y = df2['Temperature']
    lr = linear_model.LinearRegression()
    lr.fit(df_x, df_y)
    y_predict = lr.predict(df_x)
    average_predicted_temperature = np.average(y_predict)

    return [
            html.P('{0:,.0f}°C'.format(average_predicted_temperature),
                   className = 'predict_forecast_value'
                   ),
        ]


@app.callback(Output('forecast_time', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time_name = now.strftime('%H:%M:%S')

    if time_name > '13:00:00' and time_name <= '14:00:00':
        return [
            html.P('14:00',
                   className = 'forecast_time_value'
                   ),
    ]

    elif time_name > '14:00:00' and time_name <= '15:00:00':
        return [
            html.P('15:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '15:00:00' and time_name <= '16:00:00':
        return [
            html.P('16:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '16:00:00' and time_name <= '17:00:00':
        return [
            html.P('17:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '17:00:00' and time_name <= '18:00:00':
        return [
            html.P('18:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '18:00:00' and time_name <= '19:00:00':
        return [
            html.P('19:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '19:00:00' and time_name <= '20:00:00':
        return [
            html.P('20:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '20:00:00' and time_name <= '21:00:00':
        return [
            html.P('21:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '21:00:00' and time_name <= '22:00:00':
        return [
            html.P('22:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '22:00:00' and time_name <= '23:00:00':
        return [
            html.P('23:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '23:00:00' and time_name <= '23:59:59':
        return [
            html.P('00:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name >= '00:00:00' and time_name <= '01:00:00':
        return [
            html.P('01:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '01:00:00' and time_name <= '02:00:00':
        return [
            html.P('02:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '02:00:00' and time_name <= '03:00:00':
        return [
            html.P('03:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '03:00:00' and time_name <= '04:00:00':
        return [
            html.P('04:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '04:00:00' and time_name <= '05:00:00':
        return [
            html.P('05:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '05:00:00' and time_name <= '06:00:00':
        return [
            html.P('06:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '06:00:00' and time_name <= '07:00:00':
        return [
            html.P('07:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '07:00:00' and time_name <= '08:00:00':
        return [
            html.P('08:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '08:00:00' and time_name <= '09:00:00':
        return [
            html.P('09:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '09:00:00' and time_name <= '10:00:00':
        return [
            html.P('10:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '10:00:00' and time_name <= '11:00:00':
        return [
            html.P('11:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '11:00:00' and time_name <= '12:00:00':
        return [
            html.P('12:00',
                   className = 'forecast_time_value'
                   ),
    ]
    elif time_name > '12:00:00' and time_name <= '13:00:00':
        return [
            html.P('13:00',
                   className = 'forecast_time_value'
                   ),
    ]


@app.callback(Output('status_temperature', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    convert_c_t_fahrenheit = (get_temp * 9/5) + 32
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)
    convert_kph_to_mph = get_wind_speed / 1.609344
    raise_power = convert_kph_to_mph ** 0.16
    feels_like = 35.74 + (0.6215 * convert_c_t_fahrenheit) - (35.75 * raise_power) + (0.4275 * convert_c_t_fahrenheit * raise_power)
    convert_f_t_c = (feels_like - 32) * 5/9
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100

    if get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('night-rain.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Rain',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    if get_rain_value >= 800.0 and get_rain_value <= 900.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('rain.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Showers',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    if get_rain_value < 800.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('rain.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Rain',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
    elif get_photo_resistor_value < 300.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('moon.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Clear',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb > 1002.00 and convert_pa_to_mb <= 1005.00:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('moon.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Clear',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb >= 1000.00 and convert_pa_to_mb < 1002.00:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('fog-moon.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Fog',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]
    elif get_photo_resistor_value >= 300.0 and get_photo_resistor_value <= 800.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('cloud.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Cloudy',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    elif get_photo_resistor_value > 800.0 and get_photo_resistor_value <= 900.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('partly-cloud.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Partly cloudy',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]

    elif get_photo_resistor_value > 900.0:
        return [
            html.Div([
                html.Div([
                    html.Img(src = app.get_asset_url('sunny.png'),
                             className = 'image_position'),
                    html.P('{0:,.2f}°C'.format(get_temp),
                           className = 'status_temperature'
                           ),
                ], className = 'image_position_status_temperature'),

                html.Div([
                    html.P('Sunny',
                           className = 'status_temperature_right'
                           ),
                    html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(convert_f_t_c),
                           className = 'status_temperature_right_temperature'
                           ),
                ], className = 'status_temperature_right_temperature_column')
            ], className = 'status_temperature_right_temperature_row'),
        ]


@app.callback(Output('first_sentence', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')

    if get_rain_value <= 800.0 and get_led_on == ' LED ON ':
        return [
            html.P('Rain is expected during the night.',
                   className = 'status_paragraph_format'),
        ]
    if get_rain_value <= 800.0:
        return [
            html.P('Rain is expected during the day.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value < 300.0:
        return [
            html.P('The skies will be cleared.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb > 1002.00 and convert_pa_to_mb <= 1005.00:
        return [
            html.P('The skies will be cleared.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value < 300.0 and convert_pa_to_mb >= 1000.00 and convert_pa_to_mb < 1002.00:
        return [
            html.P('The skies will be foggy.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value >= 300.0 and get_photo_resistor_value <= 800.0:
        return [
            html.P('The skies wil be cloudy.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value > 800.0 and get_photo_resistor_value <= 900.0:
        return [
            html.P('The skies wil be partly cloudy.',
                   className = 'status_paragraph_format'),
        ]
    elif get_photo_resistor_value > 900.0:
        return [
            html.P('The skies wil be sunny.',
                   className = 'status_paragraph_format'),
        ]


@app.callback(Output('second_sentence', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0]
    df2 = df[['Humidity', 'Temperature']].tail(100)
    df_x = df2.drop(['Temperature'], axis = 1)
    df_y = df2['Temperature']
    lr = linear_model.LinearRegression()
    lr.fit(df_x, df_y)
    y_predict = lr.predict(df_x)
    average_predicted_temperature = np.average(y_predict)
    max_predicted_temperature = np.max(y_predict)
    min_predicted_temperature = np.min(y_predict)

    if get_temp <= average_predicted_temperature:
        return [
            html.P('The low will be ' + '{0:,.0f}°C'.format(min_predicted_temperature) + '.',
                   className = 'status_paragraph_format'),
        ]
    elif get_temp >= average_predicted_temperature:
        return [
            html.P('The high will be ' + '{0:,.0f}°C'.format(max_predicted_temperature) + '.',
                   className = 'status_paragraph_format'),
        ]


@app.callback(Output('third_sentence', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    get_temp_add = df['Temperature'].tail(1).iloc[0].astype(float) + 3.00
    get_temp_subtract = df['Temperature'].tail(1).iloc[0].astype(float) - 3.00
    get_photo_resistor_value = df['Photo Resistor Value'].tail(1).iloc[0].astype(float)
    get_rain_value = df['Rain'].tail(1).iloc[0].astype(float)
    get_led_on = df['Photo Resistor LED'].tail(1).iloc[0]
    now = datetime.now()
    day = now.strftime('%a')
    date_now = now.strftime('%d/%m/%Y')
    time_now = now.strftime('%H:%M:%S')

    if get_temp >= 1.00 and get_temp <= 4.00:
        return [
            html.P('Temperatures near freezing.',
                   className = 'status_paragraph_format'),
        ]
    else:
        []


@app.callback(Output('numeric_value', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_humidity = df['Humidity'].tail(1).iloc[0].astype(float)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    dew_point = get_temp - ((100 - get_humidity) / 5)
    get_wind = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    unique_date = df['Date'].unique()
    wind_gusts = df[df['Date'] == unique_date[-1]]['Wind Speed KPH'].max()

    return [
        html.Div([
            html.Div([
                html.P('HUMIDITY',
                       className = 'text_value'
                       ),
                html.Div([
                    html.P('{0:,.0f}%'.format(get_humidity),
                           className = 'number_value'
                           ),
                    html.Img(src = app.get_asset_url('humidity.png'),
                             className = 'number_image'
                             ),
                ], className = 'number_value_number_image')
            ], className = 'number_value_number_image_column'),

            html.Div([
                html.P('WIND',
                       className = 'text_value'
                       ),
                html.Div([
                    html.P('{0:,.2f} kph'.format(get_wind),
                           className = 'number_value'
                           ),
                    html.Img(src = app.get_asset_url('wind.png'),
                             className = 'number_image'
                             ),
                ], className = 'number_value_number_image')
            ], className = 'number_value_number_image_column'),

            html.Div([
                html.P(['WIND GUSTS',
                       ], className = 'text_value'
                       ),
                html.Div([
                    html.P('{0:,.2f} kph'.format(wind_gusts),
                           className = 'number_value'
                           ),
                    html.Img(src = app.get_asset_url('hurricane.png'),
                             className = 'number_image'
                             ),
                ], className = 'number_value_number_image')
            ], className = 'number_value_number_image_column'),

            html.Div([
                html.P('ATM PRESSURE',
                       className = 'text_value'
                       ),
                html.Div([
                    html.P('{0:,.2f} mb'.format(convert_pa_to_mb),
                           className = 'number_value'
                           ),
                    html.Img(src = app.get_asset_url('air.png'),
                             className = 'number_image'
                             ),
                ], className = 'number_value_number_image')
            ], className = 'number_value_number_image_column'),

            html.Div([
                html.P('DEW POINT',
                       className = 'text_value'
                       ),
                html.Div([
                    html.P('{0:,.2f}°C'.format(dew_point),
                           className = 'number_value'
                           ),
                    html.Img(src = app.get_asset_url('dew.png'),
                             className = 'number_image'
                             ),
                ], className = 'number_value_number_image')
            ], className = 'number_value_number_image_column')

        ], className = 'all_numeric_value_row'),
    ]


@app.callback(Output('air_pressure', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)
    convert_pa_to_mb = get_air_pressure / 100

    if convert_pa_to_mb < 1013.00:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('atmospheric-pressure.png'),
                         className = 'atmospheric_image'
                         ),
                html.Div([
                    html.P('ATMOSPHERIC PRESSURE',
                           className = 'air_pressure_text_value'
                           ),

                    html.P('{0:,.2f} mb'.format(convert_pa_to_mb),
                           className = 'air_value'
                           ),
                    html.P('Falling',
                           className = 'falling_rising_value'
                           ),
                ], className = 'air_pressure_text_air_value')
            ], className = 'air_pressure_text_air_value_row'),

        ]

    elif convert_pa_to_mb > 1013.00:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('atmospheric-pressure.png'),
                         className = 'atmospheric_image'
                         ),
                html.Div([
                    html.P('ATMOSPHERIC PRESSURE',
                           className = 'air_pressure_text_value'
                           ),

                    html.P('{0:,.2f} mb'.format(convert_pa_to_mb),
                           className = 'air_value'
                           ),
                    html.P('Rising',
                           className = 'falling_rising_value'
                           ),
                ], className = 'air_pressure_text_air_value')
            ], className = 'air_pressure_text_air_value_row'),

        ]


@app.callback(Output('air_quality', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_air_quality = df['CO2 Level'].tail(1).iloc[0].astype(float)

    if get_air_quality >= 250.0 and get_air_quality <= 400.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Excellent',
                               className = 'air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]

    elif get_air_quality > 400.0 and get_air_quality <= 1000.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Good',
                               className = 'air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]
    elif get_air_quality > 1000.0 and get_air_quality <= 2000.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Poor',
                               className = 'poor_air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]
    elif get_air_quality > 2000.0 and get_air_quality <= 5000.0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('air-quality.png'),
                         className = 'quality_image'
                         ),
                html.Div([
                    html.P('AIR QUALITY',
                           className = 'air_quality_text_value'
                           ),
                    html.Div([
                        html.P('{0:,.0f} ppm'.format(get_air_quality),
                               className = 'quality_value'
                               ),
                        html.P('Dangerous',
                               className = 'poor_air_quality_text_status')
                    ], className = 'air_quality_text_status_row')
                ], className = 'air_quality_text_quality_value')
            ], className = 'air_quality_text_quality_value_row'),

        ]


@app.callback(Output('sun_rise_status', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time_name = now.strftime('%H:%M:%S')
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = df['Date Time'].dt.time
    df['Time'] = df['Time'].astype(str)
    unique_date = df['Date'].unique()
    filter_led_date_2 = df[df['Date'] == unique_date[-2]][['Date', 'Photo Resistor LED', 'Time']]
    sun_rise_time_2 = filter_led_date_2[(filter_led_date_2['Photo Resistor LED'] == ' LED OFF ')]['Time'].head(1).iloc[0]
    filter_led_date_1 = df[df['Date'] == unique_date[-1]][['Date', 'Photo Resistor LED', 'Time']]
    sun_rise_time_1 = filter_led_date_1[(filter_led_date_1['Photo Resistor LED'] == ' LED ON ') &
                                        (filter_led_date_1['Time'] >= '03:00:00') &
                                        (filter_led_date_1['Time'] <= '06:00:00')]['Time'].tail(1).iloc[0]

    if time_name >= '00:00:00' and time_name <= '08:20:00':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunrise.png'),
                         className = 'sunrise_image'
                         ),
                html.P('SUNRISE',
                       className = 'sunrise_value'
                       ),
                html.P(
                       sun_rise_time_2,
                       className = 'sunrise_text_value'
                       ),
            ], className = 'sunrise_column'),
        ]
    elif time_name > '08:20:00' and time_name <= '23:59:59':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunrise.png'),
                         className = 'sunrise_image'
                         ),
                html.P('SUNRISE',
                       className = 'sunrise_value'
                       ),
                html.P(
                       sun_rise_time_1,
                       className = 'sunrise_text_value'
                       ),
            ], className = 'sunrise_column'),
        ]


@app.callback(Output('sun_set_status', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time_name = now.strftime('%H:%M:%S')
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    df['Date Time'] = pd.to_datetime(df['Date Time'])
    df['Date'] = df['Date Time'].dt.date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = df['Date Time'].dt.time
    unique_date = df['Date'].unique()
    filter_led_date_2 = df[df['Date'] == unique_date[-2]][['Date', 'Photo Resistor LED', 'Time']]
    sun_set_time_2 = filter_led_date_2[(filter_led_date_2['Photo Resistor LED'] == ' LED ON ')]['Time'].head(1).iloc[0]
    filter_led_date_1 = df[df['Date'] == unique_date[-1]][['Date', 'Photo Resistor LED', 'Time']]
    sun_set_time_1 = filter_led_date_1[(filter_led_date_1['Photo Resistor LED'] == ' LED OFF ')]['Time'].tail(1).iloc[0]

    if time_name >= '00:00:00' and time_name <= '16:30:00':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunset.png'),
                         className = 'sunset_image'
                         ),
                html.P('SUNSET',
                       className = 'sunset_value'
                       ),
                html.P(
                       sun_set_time_2,
                       className = 'sunset_text_value'
                       ),
            ], className = 'sunset_column'),
        ]
    elif time_name > '16:30:00' and time_name <= '23:59:59':
        return [
            html.Div([
                html.Img(src = app.get_asset_url('sunset.png'),
                         className = 'sunset_image'
                         ),
                html.P('SUNSET',
                       className = 'sunset_value'
                       ),
                html.P(
                       sun_set_time_1,
                       className = 'sunset_text_value'
                       ),
            ], className = 'sunset_column'),
        ]


@app.callback(Output('wind_speed', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)

    if get_wind_speed <= 20.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 20], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 20.00 and get_wind_speed <=30.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 30], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 30.00 and get_wind_speed <=40.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 40], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 40.00 and get_wind_speed <=50.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 50], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 50.00 and get_wind_speed <=60.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, 60], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }
    elif get_wind_speed > 60.00:
        return {
            'data': [go.Indicator(
                mode = 'gauge',
                value = get_wind_speed,
                gauge = {'axis': {'range': [None, get_wind_speed + 50.00], 'tickcolor': "white"},
                         'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                         'bordercolor': "rgb(0, 255, 255)",
                         'borderwidth': 0.5,
                         # 'threshold': {'line': {'color': "white", 'width': 2},
                         #               'thickness': 1, 'value': 7}
                         },
                # number = {'valueformat': '.2f',
                #           'font': {'size': 20},
                #           },
                domain = {'y': [0, 1], 'x': [0, 1]})],
            'layout': go.Layout(
                title = {'text': '',
                         'y': 0.8,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'
                         },
                font = dict(color = 'white'),
                paper_bgcolor = 'rgba(255, 255, 255, 0)',
                plot_bgcolor = 'rgba(255, 255, 255, 0)',
            ),
        }


@app.callback(Output('wind_speed_value', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)

    return [
            html.Div([
                html.P('WIND SPEED',
                       className = 'w_s_value'
                       ),
                html.P('{0:,.2f} kph'.format(get_wind_speed),
                       className = 'w_s_number_value'
                       ),
            ], className = 'w_s_number_value_column'),
    ]


@app.callback(Output('wind_direction_value', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Date Time', 'Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Degree', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)

    # degree_value = [112.5, 67.5, 90, 157.5, 135, 202.5, 180, 22.5, 45, 247.5, 225, 337.5, 0, 292.5, 315, 270]
    # direction_value = ["ESE", "ENE", "E", "SSE", "SE", "SSW", "S", "NNE", "NE", "WSW", "SW", "NNW", "N", "WNW", "NW",
    #                    "W"]
    # dictionary_degree_direction = {'Degree': degree_value, 'Direction': direction_value}
    # df2 = pd.DataFrame(dictionary_degree_direction)
    # df2['Degree'] = df2['Degree'].astype(float)
    # df2['Direction'] = df2['Direction'].astype(str)
    # merge_df = pd.merge(left = df,
    #                     right = df2,
    #                     how = 'inner',
    #                     left_on = ['Wind Direction'],
    #                     right_on = ['Degree'])

    get_wind_direction = df['Wind Direction'].tail(1).iloc[0]

    return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P(get_wind_direction,
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]


if __name__ == "__main__":
    app.run_server(debug = True)