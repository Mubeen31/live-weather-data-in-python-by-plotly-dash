import serial
import csv
from datetime import datetime

first = 'ESE'
second = 'ENE'
third = 'E'
fourth = 'ENE'
fifth = 'SE'
six = 'SSW'
seven = 'S'
eight = 'NNE'
nine = 'NE'
ten = 'WSW'
eleven = 'SW'
twelve = 'NNW'
thirteen = 'N'
fourteen = 'WNW'
fifteen = 'NW'
sixteen = 'W'

# copy the port from your Arduino editor
PORT = 'COM4'
ser = serial.Serial(PORT, 9600)

while True:
        message = ser.readline()
        data = message.strip().decode()
        split_string = data.split(',')  # split string
        humidity = float(split_string[0])  # convert first part of string into float
        temperature = float(split_string[1])  # convert tenth part of string into float
        rain = float(split_string[2])  # convert second part of string into float
        photoResistorValue = float(split_string[3])  # convert third part of string into float
        photoResistorLED = str(split_string[4])  # convert fourth part of string into float
        revolution = float(split_string[5])  # convert fifth part of string into float
        rpm = float(split_string[6])  # convert sixth part of string into float
        windSpeedKPH = float(split_string[7])  # convert seven part of string into float
        windDirection = float(split_string[8])  # convert eighth part of string into float
        co2Level = float(split_string[9])  # convert ninth part of string into float
        # temperature = float(split_string[9])  # convert tenth part of string into float
        airPressure = float(split_string[10])  # convert eleventh part of string into float
        # airPressure = float(0.0)  # convert eleventh part of string into float
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        # print(temperature)
        # print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
        #       windDirection, co2Level, temperature, airPressure)
        with open("weather_data.csv", "a") as f:
            writer = csv.writer(f, delimiter = ",")
            if windDirection == 112.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, first, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, first, co2Level, temperature, airPressure)
            elif windDirection == 67.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, second, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, second, co2Level, temperature, airPressure)
            elif windDirection == 90:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, third, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, third, co2Level, temperature, airPressure)
            elif windDirection == 157.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, fourth, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, fourth, co2Level, temperature, airPressure)
            elif windDirection == 135:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, fifth, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, fifth, co2Level, temperature, airPressure)
            elif windDirection == 202.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, six, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, six, co2Level, temperature, airPressure)
            elif windDirection == 180:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, seven, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, seven, co2Level, temperature, airPressure)
            elif windDirection == 22.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, eight, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, eight, co2Level, temperature, airPressure)
            elif windDirection == 45:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, nine, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, nine, co2Level, temperature, airPressure)
            elif windDirection == 247.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, ten, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, ten, co2Level, temperature, airPressure)
            elif windDirection == 225:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, eleven, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, eleven, co2Level, temperature, airPressure)
            elif windDirection == 337.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, twelve, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, twelve, co2Level, temperature, airPressure)
            elif windDirection == 0:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, thirteen, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, thirteen, co2Level, temperature, airPressure)
            elif windDirection == 292.5:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, fourteen, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, fourteen, co2Level, temperature, airPressure)
            elif windDirection == 315:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, fifteen, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, fifteen, co2Level, temperature, airPressure)
            elif windDirection == 270:
                writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH, windDirection, sixteen, co2Level, temperature, airPressure])
                print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
                      windDirection, sixteen, co2Level, temperature, airPressure)




