#ifndef ROBOT_HPP
#define ROBOT_HPP

#include <Arduino.h>
#include "sensors.hpp"


class Robot : public Sensors{
  private:
      /* Attributes */
      String rDirection;
      int velocity;     
      
      /* Mutators */
      void setVelocity(int);
      void setDirection(String);
      
  public:
      Robot(BluetoothSerial *);
      void teleopCommand(String, String);
           
  
};

#endif
