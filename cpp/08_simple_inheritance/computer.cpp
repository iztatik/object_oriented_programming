#include "computer.hpp"

using namespace std;

/* Constructor */
Computer::Computer(float battery, string model) : Device(battery){
    this -> model = model;
    return;
}

/* Other */
void Computer::runCode() const{
    cout << model << ": running code..." << endl;
    return;
}

