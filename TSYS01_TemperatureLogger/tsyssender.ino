
/* Blue Robotics TSYS01 Temperature Logger
-----------------------------------------------------------------------
Copyright Mick Phillips, 2017.

Reads a TSYS01 sensor every five seconds, and pushes the readings
over serial.
---------------------------------------------------------------------*/
#include <Wire.h>
#include "TSYS01.h"

TSYS01 sensor;

void setup() { 
  Serial.begin(9600);
  Wire.begin();
  Wire.setClock(100000);
  sensor.init();
}

void loop() {
  sensor.read();
  Serial.println(sensor.temperature()); 
  delay(5000);
}
