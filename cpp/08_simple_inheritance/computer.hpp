#ifndef COMPUTER_HPP
#define COMPUTER_HPP

#include <iostream>
#include <string>
#include "device.hpp"

/* Computer inherits from Device with Public access*/
class Computer : public Device{
    protected:
        std::string model;

    public:
	Computer(float, std::string);
	void runCode() const;
};

#endif
