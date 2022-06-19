#include "robot.hpp"

/* Constructor */
Robot::Robot(BluetoothSerial *bt) : Sensors(bt){
  velocity = 10;
  rDirection = "STOP";
}

void Robot::setVelocity(int velocity){
  this->velocity = constrain(velocity, 10, 100);
  Serial.print("Robot velocity: ");
  Serial.println(this->velocity);
  return;
}

void Robot::setDirection(String dir){
    rDirection = dir;
    if (rDirection == "Forward")
        Serial.println("Robot direction: Forward");
    else if (rDirection == "Backward")
        Serial.println("Robot direction: Backward");
    else if (rDirection == "CW")
        Serial.println("Robot direction: CW");
    else if (rDirection == "CCW")
        Serial.println("Robot direction: CCW");
    else if (rDirection == "Stop")
        Serial.println("Robot direction: Stop");
}

void Robot::teleopCommand(String selector, String value){
  if(selector == "direction")
      setDirection(value);
  else if(selector == "velocity")
      setVelocity(value.toInt());
  else if(selector == "sensors")
      setSensors();
  
  return;
}
