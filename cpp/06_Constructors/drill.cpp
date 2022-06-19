#include "drill.hpp"

using namespace std;

/* Constructor */
Drill::Drill(){
    state = false;
    temp = 24.0;
    speed = 0.0;

    return;
}

/* Mutators */
void Drill::setState(bool state){
    this->state = state;
    return;
}

void Drill::setTemp(float temp){
    this-> temp = temp;
    return;
}

void Drill::setSpeed(float speed){
    this->speed = speed;
    (speed > 100) ? temp = 100 : temp = 30 ;
    return;
}

/* Accessors */
bool Drill::getState() const { return state;}
float Drill::getTemp() const { return temp;}
float Drill::getSpeed() const { return speed;}

/* Others */
void Drill::toggleState() {
    state ? setState(false) : setState(true);   
    return;
}

void Drill::coolDown() {
    setTemp(24.0);
    return;
}

void Drill::printStatus() const{
    cout << "Drill status: " 
    << "\n 1. State: " << getState()
    << "\n 2. Temperature: " << getTemp() << "°" 
    << "\n 3. Speed: " << getSpeed() << " rpm" << endl;
    
    return;
}

void Drill::rotate(float speed){
    setSpeed(speed);
    return;
}
