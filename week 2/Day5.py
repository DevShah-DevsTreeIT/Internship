# Student Grade Manager
# Create a program to store and analyze student grades using dictionaries and lists

# list = []
# dict = {"name":"Hey" }

print("Welcome to Grade Manager,Here we will help  you manage your Grades 😊")

# Graade Calculator

name = input("Enter your Name: ")
print("Hello, ",name)
Grades = []
# num_sub = int(input("Enetr the number of subjects"))
num_sub = 4
print("Subjects: Maths,Hindi,English,Science")
for i in range(num_sub):
    elements = int(input(f"Enter the marks for each Subject: "))
    # ts = elements.split() 
    Grades.append(elements)
print("Your marks:",Grades)



avg_mrks = sum(Grades) / num_sub
highest = max(Grades)
lowest = min(Grades)

# print("Hello"+ name + "Your Average marks are:",avg_mrks)
# print("Hello"+ name + "Your Highest marks are:",highest)
# print("Hello"+ name + "Your Lowest marks are:",lowest)




# Grades = []
# num_sub = 4
# for i in range(num_sub):
    # elements = int(input(f"Enter the marks for each Subject: "))
    # # ts = elements.split() 
    # Grades.append(elements)
    # # ts = elements.split() 

total_grades = sum(Grades)/num_sub 
print("Your marks:",Grades)

if total_grades >= 90:
    print("A - distinction")
    print("Hello "+ name + " Your Highest marks are:",highest)

elif total_grades >= 80:
    print("B - Grade")
    print("Hello"+ name + "Your Highest marks are:",highest)

elif total_grades >= 70:
    print("C Grade ")
    print("Hello"+ name + "Your Average marks are:",avg_mrks)

elif total_grades >= 50:
    print("D Grade ")
    print("Hello"+ name + "Your Lowest marks are:",lowest)

else:
    print("F-Fail")