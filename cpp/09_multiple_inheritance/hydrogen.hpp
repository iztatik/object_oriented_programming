#ifndef HYDROGEN_HPP 
#define HYDROGEN_HPP 

#include <iostream>

class Hydrogen{
    protected:
	float hydrogenTank;

    public:
	Hydrogen(float);
	void runWithHydrogen(float);
	void chargeHydrogen();
};

#endif
