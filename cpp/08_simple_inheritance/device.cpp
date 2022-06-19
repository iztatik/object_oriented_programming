#include "device.hpp"

/* Constructor */
Device::Device(float battery = 100){
     this -> battery = battery;
     return;
}

/* Accessors */
float Device::getBattery() const{ return battery; }

/* Mutators */
void Device::setBattery(float battery = 50){
    this -> battery = battery;
    return;
}

/* Other */
void Device::charge(){
    setBattery(100);
    return;
}

void Device::status() const{
    std::cout << "Battery status: " << battery << "%" << std::endl;
    return;
}
