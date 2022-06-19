class person:
    def __init__(self,name=None,age=26,ocupation='engineer',nationality='mexican'):
        self.name=name
        self.age=age
        self.ocupation=ocupation
        self.nationality=nationality

    def greet(self):
        print('{} is greeting you'.format(self.name))

my_person = person('Alberto',26,'Engineer','Mexican')

print('{a} is an {b}'.format(a=my_person.name, b=my_person.ocupation))
my_person.greet()
my_person.name='Eduardo'
print(my_person.name)	    	
