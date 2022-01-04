/////humidity and temperature///////
#include "DHT.h"             // DHT sensors library
#define dhtPin 8             // This is data pin
#define dhtType DHT22        // This is DHT 22 sensor
DHT dht(dhtPin, dhtType);    // Initialising the DHT library
float humValue;           // value of humidity
float temperatureValueC;  // value of temperature in degrees Celcius
///////humidity and temperature///////

///////rain///////
int pinRain = A0;
int LEDGreen = 6;
int LEDRed = 7;
int targetValue = 500;
///////rain///////

///////photoresister///////
int pinLED = 3;
int pinPhotoresister = A1;
int photoresisterValue = 300;
///////photoresister///////

///////wind speed///////
int interruptPin = 2;
float revolutions=0;
int rpm=0; // max value 32,767 16 bit
int revo = 0;
long  startTime=0;
long  elapsedTime;
int anemometerRadius = 6;    //unit is "inch"
int diameter = 2;
int anemometerDiameter = diameter * anemometerRadius;   //(2*6) unit is "inch"
float piValue = 3.142;    //value of pi
float inchesKilometer = 39370.1;
float anemometerCircumference = anemometerDiameter * piValue;   //unit is "inch"
float circumferenceRpm = 0.00;
float divideInches = 0.00;
float speedOfAir = 0.00;
///////wind speed///////

//////wind direction//////
int windDir = A2;
int sensorExp[] = {66,84,93,126,184,244,287,406,461,599,630,702,785,827,886,945};
float dirDeg[] = {112.5,67.5,90,157.5,135,202.5,180,22.5,45,247.5,225,337.5,0,292.5,315,270};
char* dirCard[] = {"ESE","ENE","E","SSE","SE","SSW","S","NNE","NE","WSW","SW","NNW","N","WNW","NW","W"};
int sensorMin[] = {63,80,89,120,175,232,273,385,438,569,613,667,746,812,869,931};
int sensorMax[]  = {69,88,98,133,194,257,301,426,484,612,661,737,811,868,930,993};
int incoming = 0;
float angle = 0;
//////wind direction//////

//////Air Quality//////
int airQuality = A3;
int co2Level;
//////Air Quality//////

//////Atmospheric pressure and temperature//////
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>

#define BMP_SCK  (13)
#define BMP_MISO (12)
#define BMP_MOSI (11)
#define BMP_CS   (10)

Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);
//////Atmospheric pressure and temperature//////

void setup(){
  Serial.begin(9600);
///////humidity and temperature///////
  dht.begin();               // start reading the value from DHT sensor
///////humidity and temperature///////

///////rain///////
  pinMode(pinRain, INPUT);
  pinMode(LEDGreen, OUTPUT);
  pinMode(LEDRed, OUTPUT);
  digitalWrite(LEDGreen, LOW);
  digitalWrite(LEDRed, LOW);
///////rain///////

///////photoresister///////
  pinMode(pinLED, OUTPUT);              //initialize the pinLED as an output
  pinMode(pinPhotoresister, INPUT);     //initialize the pinPhotoresister as an output  
///////photoresister///////

///////wind speed///////
  pinMode(interruptPin, INPUT);           // set pin to input
///////wind speed///////

//////Atmospheric pressure and temperature//////
unsigned status;
  //status = bmp.begin(BMP280_ADDRESS_ALT, BMP280_CHIPID);
  status = bmp.begin(0x76);
  if (!status) {
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring or "
                      "try a different address!"));
    Serial.print("SensorID was: 0x"); Serial.println(bmp.sensorID(),16);
    Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
    Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
    Serial.print("        ID of 0x60 represents a BME 280.\n");
    Serial.print("        ID of 0x61 represents a BME 680.\n");
//    while (1) delay(10);
  }

  /* Default settings from datasheet. */
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */    
//////Atmospheric pressure and temperature//////
}

void loop() {
///////humidity and temperature///////
  humValue = dht.readHumidity();               // value of humidity
//  temperatureValueC = dht.readTemperature();   // value of temperature in degrees Celcius
  Serial.print(humValue);     // get value of humidity
//  Serial.print(" , ");          // create space after the value of humidity
//  Serial.print(temperatureValueC);  // get value of temperature in degrees Celcius
///////humidity and temperature///////

///////rain///////
  int rainSensor = analogRead(pinRain);
  Serial.print(" , ");          // create space
  Serial.print(rainSensor);
  if(rainSensor < targetValue){
    digitalWrite(LEDGreen, LOW);
    digitalWrite(LEDRed, HIGH);
  }
  else {
    digitalWrite(LEDGreen, HIGH);
    digitalWrite(LEDRed, LOW);
  }
///////rain///////

///////photoresister///////
  int photoresisterStatus = analogRead(pinPhotoresister);
  Serial.print(" , ");          // create space
  Serial.print(photoresisterStatus);
  if(photoresisterStatus <= photoresisterValue){
    digitalWrite(pinLED, HIGH);
//    delay(1000);
//    digitalWrite(pinLED, LOW);
//    delay(1000);
    Serial.print(" , ");          // create space
    Serial.print("LED ON");
  }
  else {
    digitalWrite(pinLED, LOW);
    Serial.print(" , ");          // create space
    Serial.print("LED OFF");
  }
///////photoresister///////

///////wind speed///////
  revolutions=0; 
  rpm=0;
  revo = 0;
  circumferenceRpm = 0.00;
  divideInches = 0.00;
  speedOfAir = 0.00;
  startTime=millis();         
  attachInterrupt(digitalPinToInterrupt(interruptPin),interruptFunction,RISING);
  delay(3000);
  detachInterrupt(interruptPin);                
//now let's see how many counts we've had from the hall effect sensor and calc the RPM
  elapsedTime=millis()-startTime;     //finds the time, should be very close to 1 sec
  if(revolutions>0) {
    rpm=(max(1, revolutions) * 60000) / elapsedTime;        //calculates rpm
    revo = revolutions;
    circumferenceRpm = anemometerCircumference * rpm;       //unit is "inches per minute"
    divideInches = circumferenceRpm / inchesKilometer;      //unit is "kilometer per minute"
    speedOfAir = divideInches * 60;                  //unit is "kilometer per hour"
    }
  Serial.print(" , ");          // create space
  Serial.print(revo);
  Serial.print(" , ");          // create space
  Serial.print(rpm);
  Serial.print(" , ");          // create space
  Serial.print(speedOfAir);
  Serial.print(" , ");
///////wind speed///////

//////wind direction//////
  incoming = analogRead(windDir);
  for(int i=0; i<=15; i++) {
    if(incoming >= sensorMin[i] && incoming <= sensorMax[i]) {
      angle = dirDeg[i];
      break;
      }
  }
  Serial.print(angle);
  Serial.print(" , ");
//////wind direction//////

//////Air Quality//////
  int airQualityData = analogRead(airQuality);
  co2Level = airQualityData - 112;
  co2Level = map(co2Level,0,1024,400,5000);
  Serial.print(co2Level);
  Serial.print(" , ");
//////Air Quality//////

////Atmospheric pressure and temperature//////
    Serial.print(bmp.readTemperature());
    Serial.print(" , ");
    Serial.println(bmp.readPressure());
////Atmospheric pressure and temperature//////
 
  delay(3000);
}
void interruptFunction() //interrupt service routine
{  
  revolutions++;
}
