#include <iostream>

using std::cin;
using std::cout;
using std::endl;

class Robot{
    public:
    	/* Attributes */
    	int steps = 3;
    	
        /* Methods */
        void turnOn(){
            cout << "Robot turned on" << endl;
            return ;
            }
        
        void walk(){
            cout << "The robot is walking continuously ..." << endl;
            return ;
            }
        /* Method overloading */
        void walk(int steps){
            if (this->steps == steps)
                cout << "The robot is walking for " << steps << " default steps" << endl;
            else
                cout << "The robot is walking for " << steps << " user defined steps" << endl;
            return ;
            }
        
};

int main(){
    int n = 0;

    /* Instance an object of the class Drill */
    Robot my_robot; 
    
    /* Turn on  */
    my_robot.turnOn();

    /* Walk for some steps */
    cout << "Number of steps: ";
    cin >> n;
    my_robot.walk(n);

    /* Walk for continuously */
    my_robot.walk();

    return 0;
}
