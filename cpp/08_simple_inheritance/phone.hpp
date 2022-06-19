#ifndef PHONE_HPP
#define PHONE_HPP

#include <iostream>
#include "computer.hpp"

class Phone : public Computer{
    protected:
	long int number;

    public:
	Phone(float, std::string, long int);
	void call();

};

#endif
