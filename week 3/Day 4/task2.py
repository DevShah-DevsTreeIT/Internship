class Shape:
        
    def base(self):
        print("\nThis is shape Calculator")
        pass

class Circle(Shape):
    def abc(self):
        print("This is a Circle\n")
     

class Rectangle(Shape):
    def abc(self):
        print("This is a Rectangle\n")

class Traingle(Shape):
    def abc(self):
        print("This is a Triangle\n")



obj1 = Shape()
obj1.base()
# obj1.abc()

obj2 = Circle()
obj2.base()
obj2.abc()

obj3 = Rectangle()
obj3.base()
obj3.abc()

obj4 = Traingle()
obj4.base()
obj4.abc()













################################ Advance #################################
# import math

# # Base class
# class Shape:
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

# # Circle subclass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print("\n--- Area of Circle ---")
#         aoc = math.pi * self.radius ** 2
#         print(f"The area of the circle with radius {self.radius} is: {aoc:.2f} cm²")

# # Triangle subclass
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         print("\n--- Area of Triangle ---")
#         aot = 0.5 * self.base * self.height
#         print(f"The area of the triangle with base {self.base} and height {self.height} is: {aot:.2f} cm²")

# # Rectangle subclass
# class Rectangle(Shape):
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def area(self):
#         print("\n--- Area of Rectangle ---")
#         aor = self.width * self.length
#         print(f"The area of the rectangle with width {self.width} and length {self.length} is: {aor:.2f} cm²")

# # Main program
# def main():
#     while True:
#         print("\n=== Shape Calculator ===")
#         print("1. Area of Circle")
#         print("2. Area of Triangle")
#         print("3. Area of Rectangle")

#         try:
#             choice = int(input("Please enter your choice (1/2/3): "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == 1:
#             radius = float(input("Enter the radius: "))
#             c = Circle(radius)
#             c.area()

#         elif choice == 2:
#             base = float(input("Enter the base: "))
#             height = float(input("Enter the height: "))
#             t = Triangle(base, height)
#             t.area()

#         elif choice == 3:
#             width = float(input("Enter the width: "))
#             length = float(input("Enter the length: "))
#             r = Rectangle(width, length)
#             r.area()

#         else:
#             print("Please enter a valid option (1/2/3).")
#             continue

#         again = input("\nDo you want to calculate another shape? (Y/N): ").lower()
#         if again != 'y':
#             print("Thanks for using the Shape Calculator. Goodbye!")
#             break

# # Start the program
# main()
