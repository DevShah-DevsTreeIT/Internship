Grades = []
num_sub = 4
for i in range(num_sub):
    elements = int(input(f"Enter the marks for each Subject: "))
    # ts = elements.split() 
    Grades.append(elements)
    # ts = elements.split() 

total_grades = sum(Grades)/num_sub 
print("Your marks:",Grades)

if total_grades >= 90:
    print("A - distinction")
elif total_grades >= 90:
    print("B - ")
elif total_grades >= 90:
    print("C - ")
elif total_grades >= 90:
    print("D - ")
else:
    print("F-Fail")