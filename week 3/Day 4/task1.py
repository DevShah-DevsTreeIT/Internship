# Animal Hierarchy :- Create Animal base class with Dog and Cat subclasses demonstrating inheritance

# is-a relationshi :-Inheritance is an is-a relationship. That is, we use inheritance only if there exists an is-a relationship between two classes.
#  For example:- Car is a Vehicle,Apple is a Fruit,Cat is an Animal


class Animal:
    # name = "" #attribute and method of parent class    
    def __init__(self,name):
        self.name = name 

    def Animal_info(self):
        print(f"I'm a {self.__class__.__name__}")

# Inherit from animal
class Dog(Animal):

    # this is a new method in subclass
    def display(self):
        # To access name attribute of superclass using self 
        print("Bhauu-Bhauu,My name is ",self.name)

class Cat(Animal):
    def display(self):
        print("Meow,My name is ",self.name)


# create an object of the subclass
labrador  = Dog("Nancy")
# To Access super class attribute and method 
labrador.display()     # this will call subclass method
labrador.Animal_info()


Persian_cat = Cat("Snowbell")
Persian_cat.display() # this will call subclass method
Persian_cat.Animal_info()