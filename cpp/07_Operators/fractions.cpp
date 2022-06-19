#include "fractions.hpp"

using namespace std;

/* Constructor: Is important to use default arguments*/
Fraction::Fraction(int num = 1, int den = 1){
    this -> num = num;
    this -> den = den;
    return;
}

/* Operator overload: Operator is passed by alias*/
/* Only an argument is necesary, the other is the object previous to the operator */
Fraction Fraction::operator +(const Fraction& fr1){
    Fraction fr2;

    fr2.den = this -> den * fr1.den;
    fr2.num = this -> num * fr1.den + this -> den *fr1.num;

    return fr2;
}

void Fraction::print(){
    cout << num << "/" << den << endl;
    return;
}
