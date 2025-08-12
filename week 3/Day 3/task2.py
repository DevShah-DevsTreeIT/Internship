# Student Management: Design a Student class with properties and methods for grade management

class Student:
    total_subjects = 4

    def __init__(self, sname, student_id, grades=None):
        self.sname = sname
        self.student_id = student_id
        self.grades = grades if grades else {}  # Initialize empty dict if not passed

    def add_grade(self, subject, grade):       
        print("################# Add Grades ##################")
        if subject in self.grades:
            print(f"{subject} already has a grade of {self.grades[subject]}. Updating it to {grade}.")
        else:
            print(f"Adding new subject {subject} with grade {grade}.")
        self.grades[subject] = grade
        print(f"Grade {grade} added/updated for subject: {subject}.")

    def remove_grade(self, subject):
        print("################# Remove Grades ##################")
        if subject in self.grades:
            del self.grades[subject]
            print(f"Grade for subject '{subject}' deleted successfully.")
        else:
            print(f"Subject '{subject}' not found in grades.")

    def calculate_average(self):
        print("################# Calculate Average ##################")
        if not self.grades:
            print("No grades available to calculate average.")
            return
        total = sum(self.grades.values())
        avg = total / len(self.grades)
        print(f"Average grade for {self.sname} is: {avg:.2f}")

    def get_highest_grade(self):
        print("################# Highest Grade ##################")
        if not self.grades:
            print("No grades available.")
            return
        subject = max(self.grades, key=self.grades.get)
        print(f"Highest grade is in {subject}: {self.grades[subject]}")

    def display_grades(self):
        print("################# Display Grades ##################")
        if not self.grades:
            print("No grades to display.")
            return
        print(f"Grades for {self.sname} (ID: {self.student_id}):")
        for subject, grade in self.grades.items():
            print(f" - {subject}: {grade}")

    def update_grade(self, subject, new_grade):
        print("################# Update Grade ##################")
        if subject in self.grades:
            self.grades[subject] = new_grade
            print(f"Grade updated for {subject}: {new_grade}")
        else:
            print(f"{subject} not found in grades. Use 'Add Grade' to add it.")


# ===================== Main Program =====================
# Create a student
name = input("Enter student name: ")
sid = input("Enter student ID: ")
s1 = Student(name, sid)

# Menu Loop
while True:
    print("\nAvailable choices:")
    print("1. Add Grade")
    print("2. Remove Grade")
    print("3. Calculate Average")
    print("4. Display Grades")
    print("5. Highest Grade")
    print("6. Update Grade")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject name: ")
        grade = int(input("Enter grade: "))
        s1.add_grade(subject, grade)

    elif choice == "2":
        subject = input("Enter subject to remove: ")
        s1.remove_grade(subject)

    elif choice == "3":
        s1.calculate_average()

    elif choice == "4":
        s1.display_grades()

    elif choice == "5":
        s1.get_highest_grade()

    elif choice == "6":
        subject = input("Enter subject to update: ")
        grade = int(input("Enter new grade: "))
        s1.update_grade(subject, grade)

    elif choice == "0":
        print("Exiting the program.")
        break

    else:
        print("Please enter a valid option.")
