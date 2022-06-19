#include <iostream>
#include "drill.hpp"

using namespace std;

int main(){

    /* Instance an object of the class Drill */
    Drill my_drill; 
    my_drill.printStatus(); 

    /* Turn on and drill at 65 rpm */
    cout << "Drilling at 65 rpm " << endl;
    my_drill.toggleState();
    my_drill.rotate(65);
    my_drill.printStatus();

    /* Incresing speed to 120 rpm*/
    cout << "Drilling at 120 rpm " << endl;
    my_drill.rotate(120);
    my_drill.printStatus();

    /* Wait to cool down and turn off */
    my_drill.coolDown();
    my_drill.toggleState();
    my_drill.printStatus();

    return 0;
}
