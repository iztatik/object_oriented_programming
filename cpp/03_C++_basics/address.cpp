#include <iostream>
#include <string>

using namespace std;

int main(){
	string food = "Pizza";	// String variable
	string* ptr = &food; 	// Pointer to string variable
	
	cout << food << endl;	// Prints the value of the string variable
	cout << &food << endl;  // Prints the direction of the string variable
	cout << ptr << endl;	// Prints the direction of the string variable
	cout << *ptr << endl;   // Prints the value of the string variable
	
	return 0;

}
