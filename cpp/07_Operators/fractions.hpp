#ifndef Fraction_HPP
#define Fraction_HPP

#include <iostream>

class Fraction{
    
    private:
	int num;
	int den;

    public:
	Fraction(int, int );
	Fraction operator + (const Fraction&);
	void print();

};

#endif
