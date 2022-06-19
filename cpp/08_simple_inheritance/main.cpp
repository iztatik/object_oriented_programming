#include <iostream>
#include "device.hpp"
#include "computer.hpp"
#include "phone.hpp"

using namespace std;

int main(){
    /* Generic device */
    cout << "1. Generic device: " << endl;
    Device my_dev(30.0);
    my_dev.status();
    my_dev.charge();
    my_dev.status();

    /* Computer */
    cout << "\n2. Computer: " << endl;
    Computer my_comp(45.2, "Y720");
    my_comp.status();
    my_comp.runCode();
    my_comp.charge();
    my_comp.status();
    
    /* Phone */
    cout << "\n3. Phone: " << endl;
    Phone my_phone(52.3, "Pine64", 722123456);
    my_phone.status();
    my_phone.runCode();
    my_phone.call();
    my_phone.charge();
    my_phone.status();
    
    return 0;
}
