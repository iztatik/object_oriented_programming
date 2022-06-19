#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int difference(int a, int b){
    if(a<0 or b<0){
	throw "negative";
    }
    if(b >= a){
	throw -1;
    }

    return a - b;
}

int main(){
    int a, b, c;

    /* Data input */
    cout << "Write the age of the Mom: ";
    cin >> a;
    cout << "Write the age of the Son: ";
    cin >> b;

    try{
        c = difference(a, b);
	cout << "Age difference: " << c << endl;
    }

    catch(const char *i){
        cout << "Age can't be " << i << endl;
    }

    catch(int i){
	cout << "Mom's age can't be lower or equal to the  Son's age" << endl;
    }
    
    return 0;
}

