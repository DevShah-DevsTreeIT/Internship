# Function Library 
import math


print("Welcome to theh function Library: \nhere are the some of the available options")

################### Area ###################
def Area():

# Area of Circle : π * r * r
    def area_circle():
        print("Area of Circle")
        r = float(input("Enter the Radius: "))  
        aoc = math.pi * (r * r)
        print(f"the area of the circle with radius {r} is: " + f"{aoc:.2f}" + " cm²")
    # area_circle()
# area of triangle :- (1/2) * base * height 
    def area_triangle():
        print("Area of Triangle")
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        aot = 0.5 * base * height
        # print(aot)/
        print(f"The area of the triangle with base {base} and height {height} is: " + f"{aot:.2f}" + " cm²")
    # area_triangle()
# Area of square :- side * side
    def area_square():
        print("Area of Square")
        side  = int(input("Enter side: "))
        aos = side * side
        print(f"the area of the square with side{side} is: ",aos)
    # area_square()

    print("Available options: ")
    print("1.Area of Circle")
    print("2.Area of Triangle")
    print("3.Area of Square")
    choice = int(input("Please Enter your chioce: "))
    if choice == 1:
        area_circle()
    elif choice == 2:
        area_triangle()
    elif choice == 3:
        area_square()
    else:
        print("Please Enter a valid Option:")


    choice = input("Wants to Continue Y(yes) or N(no): ").lower()
    if choice == 'y':
        Area()
    else:
        exit()


################ Temprature conversion ##################
    # Celsius to Fahrenheit: F = (9/5)C + 32; 
    # Fahrenheit to Celsius: C = (5/9)(F - 32); 
    # Celsius to Kelvin: K = C + 273.15; 
    # Fahrenheit to Kelvin: K = (5/9)(F - 32) + 273.15
def Temprature():

    print("Welcome to the Temprature converter ")


    def ctf():
        print("Celsius to Fahrenheit: ")
        Cel = float(input("Enter the Temprature in Celsius"))
        F = (9/5) * Cel + 32
        print(f"The temprature in Celsius to Fahrenheit is:{F}")


    def ftc():
        print("Fahrenheit to Celsius: ")
        Fah = float(input("Enter the Temprature in Fahrenheit"))
        Cel = (5/9) * (Fah - 32)
        print(f"The temprature in Fahrenheit to Celcius is:{Cel}")
    
    def ctk():
        print("Celsius to Kelvin: ")
        Cel = float(input("Enter the Temprature in Celsius"))
        K = Cel + 273.15
        print(f"The temprature in Celsius to Kelvin is:{K}")
    
    def ftk():
        print("Fahrenheit to Kelvin: ")
        Fah = float(input("Enter the Temprature in Fahrenheit"))
        K = (5/9) * (Fah - 32) + 273.15
        print(f"The temprature in Fahrenheit to Kelvin is:{K}")

    print("Available options: ")
    print("1.Celsius to Fahrenheit ")
    print("2.Fahrenheit to Celsius ")
    print("3.Celsius to Kelvin ")
    print("4.Fahrenheit to Kelvin ")
    choice = int(input("Please Enter your chioce: "))
    if choice == 1:
        ctf()
    elif choice == 2:
        ftc()
    elif choice == 3:
        ctk()
    elif choice == 4:
        ftk()
    else:
        print("Please Enter a valid Option:")

    choice = input("Wants to Continue Y(yes) or N(no): ").lower()
    if choice == 'y':
        Area()
    else:
        exit()


while True:

    print("Available options: ")
    print("1.Area")
    print("2.Temprature")
    choice = int(input("Please Choose any one from the given options:"))

    if choice == 1:
        Area()
    elif choice == 2:
        Temprature()
    else:
        print("Please Enter a Valid option")      