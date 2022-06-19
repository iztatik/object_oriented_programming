#include <iostream>
#include "hybrid.hpp"

using namespace std;

int main(){
    Hybrid my_car(50, 70, "Gas");
    my_car.printStatus();

    /* Run with gas */
    my_car.runWithGas(65);
    my_car.printStatus();

    /* Run with hydrogen */
    my_car.changeMode("Hydrogen");
    my_car.runWithHydrogen(20);
    my_car.printStatus();

    return 0;
}
