#ifndef GAS_HPP 
#define GAS_HPP 

#include <iostream>

class Gas{
    protected:
	float gasTank;

    public:
	Gas(float);
	void runWithGas(float);
	void chargeGas();
};

#endif
