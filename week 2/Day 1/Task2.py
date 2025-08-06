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

print("Hello"+ name + "Your Average marks are:",avg_mrks)
print("Hello"+ name + "Your Highest marks are:",highest)
print("Hello"+ name + "Your Lowest marks are:",lowest)

