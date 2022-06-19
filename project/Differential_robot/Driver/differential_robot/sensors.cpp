#include "sensors.hpp"

Sensors::Sensors(BluetoothSerial *bt){
  this->bt = bt;
  temperature = 0.0;
  humidity = 0.0;
  presion = 0.0;
  distance = 0.0;
}

void Sensors::readSensors(){
  temperature = readTemp();
  humidity = readHumidity();
  presion = readPresion();
  distance = readDistance();

  return;
}

void Sensors::setSensors(){
  readSensors();
  bt->print(temperature);
  bt->print('/');
  bt->print(humidity); 
  bt->print('/');
  bt->print(presion);
  bt->print('/');
  bt->print(distance);
  return;
}

float Sensors::readTemp(){
  return 26.2;
}

float Sensors::readHumidity(){
  return 1.25;
}

float Sensors::readPresion(){
  return 9.72;
}

float Sensors::readDistance(){
  return 2.5;
}
