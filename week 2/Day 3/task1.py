# Graade Calculator

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
elif total_grades >= 80:
    print("B - Grade")
elif total_grades >= 70:
    print("C Grade ")
elif total_grades >= 50:
    print("D Grade ")
else:
    print("F-Fail")