#include "hybrid.hpp"

using namespace std;

/* Constructor */
Hybrid::Hybrid(float gasTank, float hydrogenTank, string mode) : Gas(gasTank), Hydrogen(hydrogenTank){
    this -> mode = mode;
    return;
}

/* Other */
void Hybrid::changeMode(string mode){
    cout << "Change mode to: " << mode << endl;
    this -> mode = mode;
    return;
}

void Hybrid::printStatus(){
    cout << "\n     Car status " << endl;
    cout << "Mode: " << mode << endl;
    cout << "Gas tank: " << gasTank << "%" << endl;
    cout << "Hydrogen tank: " << hydrogenTank << "%\n" << endl;
    return;
}
