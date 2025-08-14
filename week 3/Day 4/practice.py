# ######################## Inheritance Types
# # There are 5 different types of inheritance in Python. They are:

# # Single Inheritance: a child class inherits from only one parent class.
# # MulGSTle Inheritance: a child class inherits from mulGSTle parent classes.
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
# Enter GST percentage (like 15): 10

# GST amount: ₹50.00
# Total bill: ₹550.00

# Would you like to split the bill? (yes/no): yes
# How many people? 3

# Each person pays: ₹183.33

class Hotel:
    def __init__(self):
        self.amount = 0
        self.GST_percentage = 5
        self.GST_amount = 0
        self.total = 0
        self.stotal = 0
        self.deduction = 0 
    def get_inputs(self):
        self.amount = float(input("Enter the bill amount: ₹"))
        # self.GST_percentage = float(input("Enter the GST percentage (%): ")) ##GST##
        self.GST_amount = (self.GST_percentage / 100) * self.amount  ##GST##

    def calculate_total(self):
        self.total = self.amount + self.GST_amount
        print(f"\n--- Bill Summary ---")
        print(f"Bill Amount: ₹{self.amount}")
        print(f"GST ({self.GST_percentage}%): ₹{self.GST_amount:.2f}") ##GST##
        print(f"Total Amount to Pay: ₹{self.total:.2f}")
        self.stotal = self.total
    # def total(self):


class Bill(Hotel):

        
    def split(self):
        while True:
            choice = str(input("Would you like to split the bill:- Y or N: ")).lower()
            if choice == 'y':
                    people = int(input("How many people?"))
                    print(f"Okay, so you are a total of {people} peoples in group.")
                    print("Avaliable options for you guys are: ")
                # while True:
                    print(f"1.Split the bill in {people} parts?")
                    print("2.Wants to pay customized amount per person.")
                    # option = ()
                    option = int(input("Enter youce choice: "))
                    if option == 1:
                        self.total = self.total / people
                        print(f"Each person has to pay: {self.total}")
                        break
                    elif option == 2:
                        for i in range(people):
                            amt = []
                            # print(f"please enter the amount for",i)
                            amt = int(input(f"Please Enter the amount for person no. {i}: "))
                            self.deduction = (amt / 100) * self.total
                            self.stotal -= self.deduction
                            # print(f"Amount yet left to pay: {self.total}")
                            if self.stotal == 0:
                                print("Thanks for visiting.")
                                break
                            # elif self.stotal > 0:
                                # if people[i] :
                        print(f"Remaining amount : {self.stotal}")
                            # elif i<=people:
                            # print(i)
                        break
                    else:
                        print("Please enter a valid option")
                    # break
            elif choice == 'n': 
                print("Thanks for visiting our hotel :) ")
                break
            else:
                print("Please enter a valid option")
        


# Create object of the child class
obj = Bill()
obj.get_inputs()          # Inherited from Hotel
obj.calculate_total()     # Inherited from Hotel
# obj.total()
obj.split() #From Bill














######################### Basic - beginning one 


# def split(self):
#             while True:
#                 choice = str(input("Would you like to split the bill:- Y or N: ")).lower()
#                 if choice == 'y':
                
#                     people = int(input("How many people?"))
#                     print(f"Okay, so you are a total of {people} peoples in group.")
#                     print("Avaliable options for you guys are: ")
#                     print(f"1.Split the bill in {people} parts?")
#                     print("2.Wants to pay customized amount per person.")

#                     option = int(input("Enter youce choice"))
#                     if option == 1:
#                         self.total = self.total / people
#                         print(f"Each person has to pay: {self.total}")
#                     elif option == 2:
#                         print("")
#                     break
                
                
#                 elif choice == 'n': 
#                     print("Thanks for visiting our hotel :) ")
#                     break
#                 else:
#                     print("Please enter a valid option")
#         split(self)

########################################












###################
# class Book:
#     def __init__(self,title = "My Personal Diary",author = "Aayushi Saini",year = 2026 ):
#         self.title = title
#         self.author = author
#         self.year = year
        


#     def get_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Year: {self.year}")


# obj1 = Book()
# obj1.get_info()

# #################
# class Student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
    
#     def is_passed(self):
#         return self.marks >= 40
#             # print("Pass") #this is a comment

# obj1 = Student(name = "Joy",marks= 45,age =54)
# # print(obj1.is_passed())

# #for Printing the result
# if obj1.is_passed():
#     print(f"{obj1.name} you are pass ")
# else:
#     print(f"{obj1.name} You are fail")