#include <iostream>
using std::cout;
using std::endl;

// first name space
namespace firstSpace {
   int num = 1;
   void func() {
      cout << "Inside namespace: " << num << endl;
   }
}

// second name space
namespace secondSpace {
   int num = 2;
   void func() {
      cout << "Inside namespace: " << num << endl;
   }
}

int main () {
   // Calls function from first name space.
   firstSpace::func();
   
   // Calls function from second name space.
   secondSpace::func(); 

   return 0;
}
