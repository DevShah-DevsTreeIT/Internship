# ######################## Inheritance Types
# # There are 5 different types of inheritance in Python. They are:

# # Single Inheritance: a child class inherits from only one parent class.
# # Multiple Inheritance: a child class inherits from multiple parent classes.
# # Multilevel Inheritance: a child class inherits from its parent class, which is inheriting from its parent class.
# # Hierarchical Inheritance: more than one child class are created from a single parent class.
# # Hybrid Inheritance: combines more than one form of inheritance.


# ######################## Uses of Inheritance
# # Code Reusability: Since a child class can inherit all the functionalities of the parent's class, this allows code reusability.
# # Efficient Development: Once a functionality is developed, we can simply inherit it which allows for cleaner code and easy maintenance.
# # Customization: Since we can also add our own functionalities in the child class, we can inherit only the useful functionalities and define other required features.



# ###########################
# # class person:
# #     def __init__(self,fname,lname):
# #         self.fname = fname
# #         self.lname = lname
        
# #     def printname(self):
# #         print(f"First name:{self.fname} and last name: {self.lname}")


# # class Student(person):
    
# #     def tp(self):
# #         print(f"{self.fname}  {self.lname}")

# #     pass

# # x = Student("John","Cena")

# # x.tp()
# # x.printname()



# # Date: 11 - 08 - 2025

# # Method Overriding in Python Inheritance
# # what if the same method is present in both the superclass and subclass?

# # In this case, the method in the subclass overrides the method in the superclass. This concept is known as method overriding in Python. 
# # Example: Method Overriding




# class Animal:
#     def __init__(self):
#         pass
#     def Age(self):
#         print("I'm 4 years old.")    

      
# class Dog(Animal):
    

#     def Age(self):    # This overides the age method from base class
#         print("I'm just 2 years old puppy")
#     def Bark(self):
#         print("Hey,from Dog ")

# class Cat(Animal):

#     def Meow(self):
#         print("Hello, from Cat ")
    
#     def Age(self): 
#         super().Age()  # call the eat() method of the superclass using super() keyword.
#         print("My age is 12:")


# obj1 = Dog()
# obj1.Age()
# obj1.Bark()

# print("\n")

# obj2 = Cat()
# obj2.Age()
# obj2.Meow()
# # ####

# # class polygon - def init,display_info,get_peri
# # class triangle(polygon):
# #     pass
# # class Quadrilateral(polygon):
# #     pass

# # obj1



# class Polygon:
#     def __init__(self,slides):
#         self.sides = slides

#     def display_info(self,sides):    
    
#     def get_perimeter():
        
#         pass
# class Triangle(Polygon):
#     def display_info(self):
#         print("A Triangle is a polygon with 3 edges")    

# class Quadrilateral(Polygon):
#     def display_info(self):
#         print("A Quadrilateral is a polygon with 4 Edges")
#     pass


# T1 = Triangle([5,6,7])
# perimeter = T1.get_perimeter()
# print("The perimeter is ")



# Enter bill amount: 500
# Enter tip percentage (like 15): 10

# Tip amount: ₹50.00
# Total bill: ₹550.00

# Would you like to split the bill? (yes/no): yes
# How many people? 3

# Each person pays: ₹183.33

class Hotel:
    def __init__(self):
        self.amount = 0
        self.tip_percentage = 0
        self.tip_amount = 0

    def get_inputs(self):
        self.amount = float(input("Enter the bill amount: ₹"))
        self.tip_percentage = float(input("Enter the tip percentage (%): "))
        self.tip_amount = (self.tip_percentage / 100) * self.amount


class Bill(Hotel):
    def calculate_total(self):
        total = self.amount + self.tip_amount
        print(f"\n--- Bill Summary ---")
        print(f"Bill Amount: ₹{self.amount}")
        print(f"Tip ({self.tip_percentage}%): ₹{self.tip_amount:.2f}")
        print(f"Total Amount to Pay: ₹{total:.2f}")
        def split(self):
            while True:
                choice = str(input("Would you like to split the bill:- Y or N: ")).lower()
                if choice == 'y':
                    people = int(input("How many people?"))
                    self.total = total / people
                    print(f"Each person has to pay: {self.total}")
                    break
                elif choice == 'n': 
                    print("Thanks for visiting our hotel :) ")
                    break
                else:
                    print("Please enter a valid option")
        split(self)


# Create object of the child class
obj = Bill()
obj.get_inputs()          # Inherited from Hotel
obj.calculate_total()     # From Bill