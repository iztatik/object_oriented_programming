#include <iostream>
#include <stdexcept>

using std::cin;
using std::cout;
using std::endl;

class DivisionByZeroException : public std::runtime_error{
    public:
	DivisionByZeroException() : std::runtime_error("Attempted to divide by zero"){}
};

double divide(double num, double den){
    if(den==0)
	throw DivisionByZeroException();

    return num/den;
}

int main(){
    double a, b, c;

    cout << "Write a number: ";
    cin >> a;
    cout << "Write another number: ";
    cin >> b;

    try{
        c = divide(a, b);
        cout << "The division is: " << c << endl;
    }

    catch(DivisionByZeroException &myException){
	cout << "Error: " << myException.what() << endl;
    }

    return 0;
}

