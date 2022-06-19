#ifndef DEVICE_HPP
#define DEVICE_HPP

#include <iostream>

class Device{
    protected:
        float battery;
	void setBattery(float);
	float getBattery() const;

    public:
	Device(float);
	void charge();
	void status() const;

};
#endif
