#include "gas.hpp"

using namespace std;

/* Constructor */
Gas::Gas(float gasTank){
    this -> gasTank = gasTank;
    return;
}

/* Other */
void Gas::runWithGas(float dist){
    (dist > 60 ) ? gasTank = 10 : gasTank = 30;
    cout << "Running with gas for " << dist << " km ..." << endl;
    return;

}

void Gas::chargeGas(){
    gasTank = 100;
    return;
}
