#include "hydrogen.hpp"

using namespace std;

/* Constructor */
Hydrogen::Hydrogen(float hydrogenTank){
    this -> hydrogenTank = hydrogenTank;
    return;
}

/* Other */
void Hydrogen::runWithHydrogen(float dist){
    (dist > 60 ) ? hydrogenTank = 10 : hydrogenTank = 30;
    cout << "Running with hydrogen for " << dist << " km ..." << endl;
    return;

}

void Hydrogen::chargeHydrogen(){
    hydrogenTank = 100;
    return;
}
