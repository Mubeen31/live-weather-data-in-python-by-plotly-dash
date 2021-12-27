import serial
import csv
from datetime import datetime

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
        # airPressure = float(split_string[10])  # convert eleventh part of string into float
        airPressure = float(0.0)  # convert eleventh part of string into float
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        # print(temperature)
        print(dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm, windSpeedKPH,
              windDirection, co2Level, temperature, airPressure)
        with open("weather_data.csv", "a") as f:
            writer = csv.writer(f, delimiter = ",")
            # writer.writerow(['Time', 'Humidity', 'Temperature'])
            writer.writerow([dt_string, humidity, rain, photoResistorValue, photoResistorLED, revolution, rpm,
                             windSpeedKPH, windDirection, co2Level, temperature, airPressure])
