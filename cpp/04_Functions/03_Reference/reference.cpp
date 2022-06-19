#include <iostream>
#include "change.hpp"

using namespace std;

int main(){
   int n1 = 3;
   int n2 = 7;

   cout << "Original order: n1 = " << n1 << " n2 = " << n2 << endl;

   changeAlias(n1, n2);
   cout << "Change by Alias: n1 = " << n1 << " n2 = " << n2 << endl;

   changePointer(&n1, &n2);
   cout << "Change by Pointer: n1 = " << n1 << " n2 = " << n2 << endl;

   return 0;
}
