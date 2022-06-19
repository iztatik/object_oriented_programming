#include <iostream>

using namespace std;

class Instrument{
    public:
	virtual void makeSound() = 0;
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

class Piano: public Instrument{
    public:
	void makeSound(){
	    cout << "Piano playing..." << endl;
	};
};


int main(){
    /* Pointers array */
    Instrument* instruments[3] = {new Accordion, new Violin, new Piano};

    /* Play all instruments */
    for(int i=0; i<3; i++)
	instruments[i] -> makeSound();

    return 0;
}
