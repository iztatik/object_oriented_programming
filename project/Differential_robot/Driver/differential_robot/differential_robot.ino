#include "BluetoothSerial.h"
#include "robot.hpp"

BluetoothSerial SerialBT;
Robot myRobot(&SerialBT);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  SerialBT.begin("ESP32_robot");
  Serial.println("Waiting for a bluetooth connection...");
}

String selector = "";
String value = "";

void loop() {
  while(!SerialBT.available()){;}
  selector = SerialBT.readStringUntil('/');
  value = SerialBT.readStringUntil('/');
  myRobot.teleopCommand(selector, value);    
  
  delay(50);
}
