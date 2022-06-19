#include "phone.hpp"

using namespace std;


/* Constructor */
Phone::Phone(float battery, string model, long int number) : Computer(battery, model){
	this -> number = number;
	return;
}


/* Other */
void Phone::call(){
    cout << model << " making a call from " << number << " number " << endl;
    return;
}

