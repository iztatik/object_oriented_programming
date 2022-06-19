#ifndef DRILL_HPP
#define DRILL_HPP

#include <iostream>

class Drill{
    
    private:
	/* Attributes */
	bool state;
	float temp;
	float speed;

	/* Mutators */
	void setState(bool);
	void setTemp(float);
	void setSpeed(float);

    public:
	Drill();
	
	/* Accessors */
	bool getState() const;
	float getTemp() const;
	float getSpeed() const;

	/* Other */
	void toggleState() ;
	void coolDown() ;
        void printStatus() const;	
	void rotate(float);

};

#endif
