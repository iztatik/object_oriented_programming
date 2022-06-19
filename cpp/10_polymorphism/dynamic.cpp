#include <iostream>

using namespace std;

class Instrument{
    public:
	virtual void makeSound(){
	    cout << "Instrument playing..." << endl; 
	}
};

class Accordion : public Instrument{
    public:
	void makeSound(){
	    cout << "Accordion playing..." << endl;
	};
};

class Violin: public Instrument{
    public:
	void makeSound(){
	    cout << "Violin playing..." << endl;
	};

};

class Other: public Instrument{};

int main(){
    /* Objects */
    Instrument my_instrument;
    Accordion my_accordion;

    /* Pointers */
    Instrument* my_instrument_ptr = &my_instrument;
    Instrument* my_accordion_ptr = &my_accordion;
    Instrument* my_violin_ptr = new Violin;
    Instrument* my_other_ptr = new Other;

    my_instrument_ptr -> makeSound();
    my_accordion_ptr -> makeSound();
    my_violin_ptr -> makeSound();
    my_other_ptr -> makeSound();

    return 0;
}
