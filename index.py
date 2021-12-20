import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime


font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 3000,
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
            ], className = 'title_image_value_row')
        ], className = 'title_date_time_container')
    ], className = 'title_date_time_container_overlay'),

    html.Div([
        html.Div(id = 'background_image_container',
                 className = 'background_image'),
        html.Div([
            html.Div(id = 'time_value')
        ], className = 'current_weather_time_value')
    ], className = 'background_image_current_weather_time_column'),

    html.Div(id = 'status_temperature',
             className = 'status_temperature_value'),

    html.Div(id = 'status_paragraph',
             className = 'status_paragraph_value'),

    html.Div(id = 'numeric_value',
             className = 'status_numeric_value'),

    html.Div(className = 'background_color_more_details'),
    html.Div([
        html.Div(className = 'more_details_bottom_border'),
    ], className = 'more_details_bottom_border_row'),
    html.P('More Details',
           className = 'more_details'),

    html.Div(className = 'background_color_more_details_card'),
    html.Div(id = 'uv_index',
             className = 'uv_index_value'),
    html.Div(id = 'air_pressure',
             className = 'air_pressure_value'),
    html.Div(id = 'air_quality',
             className = 'air_quality_value'),

    html.Div([
        html.Div(id = 'sun_rise_status'),
        html.Img(src = app.get_asset_url('climate.png'),
                 className = 'circle_image'),
        html.Div(id = 'sun_set_status'),
    ], className = 'sun_rise_set_status_value'),

    html.Div(className = 'background_sun_rise_set_right_border'),

    html.Div([
        dcc.Graph(id = 'wind_speed',
                  animate = False,
                  config = {'displayModeBar': False},
                  className = 'wind_speed_graph'),
        html.Div(id = 'wind_speed_value',
                 className = 'wind_speed_numeric_value')
    ], className = 'wind_speed_numeric_value_column'),

    html.Div(id = 'wind_direction_value',
             className = 'wind_speed_direction_numeric_value')

])


@app.callback(Output('title_image_value', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)

    return [
        html.Div([
            html.Img(src = app.get_asset_url('fog.png'),
                     className = 'cloud_image'),
            html.P('{0:,.0f}°C'.format(get_temp),
                   className = 'temperature_value'
                   ),
        ], className = 'image_value'),
    ]


@app.callback(Output('background_image_container', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)

    return [
        html.Div(style = {'background-image': 'url("/assets/fog.jpg")',
                          'background-repeat': 'no-repeat',
                          'background-size': 'auto'
                          },
                 className = 'background_image_container'),
    ]


@app.callback(Output('time_value', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
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


@app.callback(Output('status_temperature', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    feels_like = df['Temperature'].tail(1).iloc[0].astype(float) - 20

    return [
        html.Div([
            html.Div([
                html.Img(src = app.get_asset_url('fog.png'),
                         className = 'image_position'),
                html.P('{0:,.0f}°C'.format(get_temp),
                       className = 'status_temperature'
                       ),
            ], className = 'image_position_status_temperature'),

            html.Div([
                html.P('Fog',
                       className = 'status_temperature_right'
                       ),
                html.P('FEELS LIKE' + ' ' + ' ' + '{0:,.0f}°C'.format(feels_like),
                       className = 'status_temperature_right_temperature'
                       ),
            ], className = 'status_temperature_right_temperature_column')
        ], className = 'status_temperature_right_temperature_row'),
    ]


@app.callback(Output('status_paragraph', 'children'),
              [Input('update_time', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_temp = df['Temperature'].tail(1).iloc[0].astype(float)
    now = datetime.now()
    day = now.strftime('%a')
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%H:%M:%S')

    return [
        html.P('The skies will be fogy. The low or high will be ' + '{0:,.0f}°C'.format(get_temp) + '.' + ' ' + 'Temperatures near freezing.',
               className = 'status_paragraph_format'),
    ]


@app.callback(Output('numeric_value', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_humidity = df['Humidity'].tail(1).iloc[0].astype(float)
    get_wind = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)
    get_co2_level = df['CO2 Level'].tail(1).iloc[0].astype(float)
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)

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
                html.P(['CO2 LEVEL',
                       ], className = 'text_value'
                       ),
                html.Div([
                    html.P('{0:,.0f} ppm'.format(get_co2_level),
                           className = 'number_value'
                           ),
                    html.Img(src = app.get_asset_url('co2.png'),
                             className = 'number_image'
                             ),
                ], className = 'number_value_number_image')
            ], className = 'number_value_number_image_column'),

            html.Div([
                html.P('AIR PRESSURE',
                       className = 'text_value'
                       ),
                html.Div([
                    html.P('{0:,.0f} pa'.format(get_air_pressure),
                           className = 'number_value'
                           ),
                    html.Img(src = app.get_asset_url('air.png'),
                             className = 'number_image'
                             ),
                ], className = 'number_value_number_image')
            ], className = 'number_value_number_image_column'),

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
            ], className = 'number_value_number_image_column')

        ], className = 'all_numeric_value_row'),
    ]


@app.callback(Output('uv_index', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_humidity = df['Humidity'].tail(1).iloc[0].astype(float)
    get_wind = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)
    get_co2_level = df['CO2 Level'].tail(1).iloc[0].astype(float)
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)

    return [
        html.Div([
            html.Img(src = app.get_asset_url('uv.png'),
                     className = 'uv_image'
                     ),
            html.Div([
                html.P('UV INDEX',
                       className = 'uv_index_text_value'
                       ),

                html.P('0' + ' ' + '-' + ' ' + 'Low',
                       className = 'index_value'
                       ),
            ], className = 'uv_index_text_index_value')
        ], className = 'uv_index_text_index_value_row'),

    ]


@app.callback(Output('air_pressure', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_air_pressure = df['Air Pressure'].tail(1).iloc[0].astype(float)

    return [
        html.Div([
            html.Img(src = app.get_asset_url('atmospheric-pressure.png'),
                     className = 'atmospheric_image'
                     ),
            html.Div([
                html.P('AIR PRESSURE',
                       className = 'air_pressure_text_value'
                       ),

                html.P('{0:,.0f} pa'.format(get_air_pressure),
                       className = 'air_value'
                       ),
            ], className = 'air_pressure_text_air_value')
        ], className = 'air_pressure_text_air_value_row'),

    ]


@app.callback(Output('air_quality', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_air_quality = df['CO2 Level'].tail(1).iloc[0].astype(float)

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
                    html.P('Fair',
                           className = 'air_quality_text_status')
                ], className = 'air_quality_text_status_row')
            ], className = 'air_quality_text_quality_value')
        ], className = 'air_quality_text_quality_value_row'),

    ]


@app.callback(Output('sun_rise_status', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_air_quality = df['CO2 Level'].tail(1).iloc[0].astype(float)

    return [
        html.Div([
            html.Img(src = app.get_asset_url('sunrise.png'),
                     className = 'sunrise_image'
                     ),
            html.P('SUNRISE',
                   className = 'sunrise_value'
                   ),
            html.P('08:14',
                   className = 'sunrise_text_value'
                   ),
        ], className = 'sunrise_column'),
    ]


@app.callback(Output('sun_set_status', 'children'),
              [Input('update_value', 'n_intervals')])
def weather_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_air_quality = df['CO2 Level'].tail(1).iloc[0].astype(float)

    return (
        html.Div([
            html.Img(src = app.get_asset_url('sunset.png'),
                     className = 'sunset_image'
                     ),
            html.P('SUNSET',
                   className = 'sunset_value'
                   ),
            html.P('15:57',
                   className = 'sunset_text_value'
                   ),
        ], className = 'sunset_column'),
    )


@app.callback(Output('wind_speed', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph_value(n_intervals):
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_wind_speed = df['Wind Speed KPH'].tail(1).iloc[0].astype(float)

    return {
        'data': [go.Indicator(
            mode = 'gauge',
            value = get_wind_speed,
            gauge = {'axis': {'range': [None, 20], 'tickcolor': "white"},
                     'bar': {'color': "rgba(0, 255, 255, 0.3)", 'thickness': 1},
                     'bordercolor': "rgb(0, 255, 255)",
                     'borderwidth': 0.5,
                     'threshold': {'line': {'color': "white", 'width': 2},
                                   'thickness': 1, 'value': 7}
                     },
            # number = {'valueformat': '.2f',
            #           'font': {'size': 20},
            #
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
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
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
    header_list = ['Humidity', 'Rain', 'Photo Resistor Value', 'Photo Resistor LED', 'Revolution', 'RPM',
                   'Wind Speed KPH', 'Wind Direction', 'CO2 Level', 'Temperature', 'Air Pressure']
    df = pd.read_csv('weather_data.csv', names = header_list)
    get_wind_direction = df['Wind Direction'].tail(1).iloc[0].astype(float)

    if get_wind_direction == 112.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('ESE',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 67.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('ENE',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 90:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('E',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 157.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('SSE',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 135:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('SE',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 202.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('SSW',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 180:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('S',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 22.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('NNE',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 45:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('NE',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 247.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('WSW',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 225:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('SW',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 337.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('NNW',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 0:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('N',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 292.5:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('WNW',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 315:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('NW',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]
    elif get_wind_direction == 270:
        return [
            html.Div([
                html.Img(src = app.get_asset_url('compass.png'),
                         className = 'compass_image'
                         ),
                html.Div([
                    html.P('WIND DIRECTION',
                           className = 'w_d_value'
                           ),
                    html.P('W',
                           className = 'w_d_number_value'
                           ),
                ], className = 'w_d_number_value_row'),
            ], className = 'w_d_number_value_column'),
        ]


if __name__ == "__main__":
    app.run_server(debug = True)