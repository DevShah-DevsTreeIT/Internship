# class Dog:
#     # Constructor method to initialize attributes
#     def __init__(self, name, age):
#         self.name = name  # Attribute for the dog's name
#         self.age = age    # Attribute for the dog's age

#     # Method to make the dog bark
#     def bark(self):
#         return f"{self.name} says Bhau Bhau!"

#     # Method to get the dog's age in human years
#     def age_in_human_years(self):
#         return self.age * 7  # Assuming 1 dog year = 7 human years

# # Creating an object (instance) of the Dog class
# my_dog = Dog("Nancy", 3)

# # Accessing attributes
# print(f"My dog's name is {my_dog.name} and she is {my_dog.age} years old.")

# # Calling methods
# print(my_dog.bark())  # Output: Buddy says Woof!
# print(f"My dog is {my_dog.age_in_human_years()} in human years.")  # Output: 21



"""

# A Class is like an object constructor, or a "blueprint" for creating objects.

class Person:   #created a new class named "Person"

    def __init__(self,name,age): # Created a inbuilt method __init__() || Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the object is being created:
        self.name = input("enter Your name") #  The __init__() method is called automatically every time the class is being used to create a new object.
        self.age = input("Enter your age")

p1 = Person("","")  # created a object of the class Person

print(f"Your name is {p1.name} and your age is {p1.age}")

"""




"""
The __str__() Method
The __str__() method controls what should be returned when the class object is represented as a string.

If the __str__() method is not set, the string representation of the object is returned:
"""


# The string representation of an object WITHOUT the __str__() method:

# when we try to call the objecty dirctly to print namee and age by print(p1) then it will something like <__main__.Person object at 0x15039e602100>
# but when we will use the inbuilt method __str__ then it will allow us to print the attributes inside that object "p1" created for method "Person"


# class Person:
#     def __init__(self,name,age):
#             self.name = name
#             self.age = age

#     def __str__(self):
#           return f"{self.name} {self.age}"

# p1 = Person("Jayeshbhai",34)

# print(p1)




#  Create Methods
# You can create your own methods inside objects. Methods in objects are functions that belong to the object.


# class Person:
      
#     def __init__(self,name,age):   #Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
#         self.name  = name  #atttribute created for name 
#         self.age  = age   #this is the attribute we created for age


#     def myfunc(self):    #function created to greet the user 
#          print(f"Hello {self.name} your age is {self.age}")

        
# p1 = Person("John",54)

# p1.name = input("Enter  your name:").capitalize()
# p1.age = 58

# p1.myfunc() #excuting the function inside the  p1 object 







# class Person:

#     def __init__(jayesh,age): #The self parameter is a reference to the current instance of the class
#         #  It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
#         jayesh.age = age
        

#     def myfunc(abc):
#         print(f"Hey User your age is {abc.age} ")
# p1 = Person(54)
# p1.age = 57
# p1.myfunc()
# del p1.age
# p1.myfunc()
# del p1
# p1.myfunc()

# class person:
    # pass




