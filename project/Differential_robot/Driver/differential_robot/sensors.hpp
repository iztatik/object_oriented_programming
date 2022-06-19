#ifndef SENSORS_HPP
#define SENSORS_HPP

#include <Arduino.h>
#include "BluetoothSerial.h"

class Sensors{
    protected:
        /* Attributes */
        float temperature;
        float humidity;
        float presion;
        float distance;
        BluetoothSerial *bt=0;

        /* Others */
        void readSensors();
        void setSensors();
        float readTemp();
        float readHumidity();
        float readPresion();
        float readDistance();  
        
    public:
        Sensors(BluetoothSerial *);
};

#endif
