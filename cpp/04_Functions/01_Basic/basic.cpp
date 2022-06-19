#include <iostream>
#include "operations.hpp"

using namespace std;

int main(){
    char selector;
    float v1=0, v2=0;

    cout << "Select an operation (+,-,*): ";
    cin >> selector;
    
    cout << "Write a number: ";
    cin >> v1;
    cout << "Write another: ";
    cin >> v2;
    
    switch(selector){
	case '+':
	    cout << "Addition" << endl;
	    v2 = add(v1, v2);
	    cout << "Result: " << v2 << endl;
	    break;
	case '-':
	    cout << "Substraction" << endl;
	    v2 = sub(v1, v2);
	    cout << "Result: " << v2 << endl;
	    break;
	case '*': 
	    cout << "Multiplication" << endl;
	    v2 = mult(v1, v2);
	    cout << "Result: " << v2 << endl;
	    break;
	default:
	    cout << "Bad argument" << endl;
	    break;
    }
}
