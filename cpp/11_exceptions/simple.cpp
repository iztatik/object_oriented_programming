#include <iostream>

using std::cin;
using std::cout;
using std::endl;

double divide(double a, double b){
     if(b == 0.0)
	throw 0;

     return a/b;
}

int main(){
    /* Variable definition */
    double a = 0.0;
    double b = 0.0;
    double c = 0.0;

    /* Data input */
    cout << "Write a number: ";
    cin >> a;
    cout << "Write a number: ";
    cin >> b;

    /* Division */
    try{
	c = divide(a, b);
        cout << a << "/" << b << " = " << c << endl;
    }
    catch(int c){
	cout << "Imposible to solve a division by " << c << endl;
    }

    return 0;
}
