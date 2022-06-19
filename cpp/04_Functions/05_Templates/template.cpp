#include <iostream>
#include "template.hpp"

using namespace std;

int main(){
    int i1=3, i2=2;
    cout << "Int: " << maxx(i1, i2) << endl;
    cout << "Float: " << maxx(5.32, 7.25) << endl;
    cout << "Char: " << maxx('a', 'z') << endl;
    
    return 0;
}
