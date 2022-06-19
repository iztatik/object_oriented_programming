#ifndef HYBRID_HPP
#define HYBRID_HPP

#include <iostream>
#include <string>
#include "gas.hpp"
#include "hydrogen.hpp"

class Hybrid : public Gas, public Hydrogen {
    private:
	std::string mode;

    public:
	Hybrid(float, float, std::string);
	void changeMode(std::string);
	void printStatus();

};

#endif
