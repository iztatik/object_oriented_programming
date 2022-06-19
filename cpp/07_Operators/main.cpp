#include <iostream>
#include "fractions.hpp"

using namespace std;

int main(){
    /* Define the fractions to be added */
    Fraction a(1, 3);
    cout << "First fraction: " << endl;
    a.print();

    Fraction b(1, 2);
    cout << "Second fraction: " << endl;
    b.print();

    /* Operate and print result */
    Fraction c = a + b;
    cout << "Addition result: " << endl;
    c.print();

    return 0;
}
