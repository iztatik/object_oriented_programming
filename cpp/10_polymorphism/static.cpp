#include <iostream>

using namespace std;

/* Base class */
class Adder{
    public:
	int add(int a, int b){
	   return a + b;
	}

	int add(int a, int b, int c){
	    a = a + b;
	    return a + c;
	}
        
	double add(double a, double b){
	   return a + b;
	}

	double add(double a, double b, double c){
	    a = a + b;
	    return a + c;
	}
        
};


int main(){
    Adder my_adder;

    cout << "3 + 5 = " << my_adder.add(3, 5) << endl;
    cout << "3 + 5 + 4 = " << my_adder.add(3, 5, 4) << endl;
    cout << "3.3 + 5,5 = " << my_adder.add(3.3, 5.5) << endl;
    cout << "3.3 + 5.5 + 4.4 = " << my_adder.add(3.3, 5.5, 4.4) << endl;


}
