#include "change.hpp"

void changeAlias(int &x, int &y){

    int z = x;
    x = y;
    y = z;

    return;
}

void changePointer(int* x, int* y){
    
    int z = *x;
    *x = *y;
    *y = z;
    
    return;
}
