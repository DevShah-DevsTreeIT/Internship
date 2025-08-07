###### Week5 Day4: T3: Full Application Development: Build a complete application integrating all learned concepts ######


#### WEEK 1 ####
"""
Week 1

day 1:- py installation and setup ✔
day 2:- git and github basics ✔
day 3:- variables and data types ✔
day 4:- basic input/output & Operators ✔
    day 5:-  Personal Calculator ❌

"""
####    ####


#### WEEK 2 #### 
"""
Week 2

day 1:- Lists and Tuple ✔
day 2:- Dictionaries and Sets ✔
day 3:- Conditional Statements ✔
day 4:- Loops ✔
    day 5:- Student Grade Manager ✔

"""
####    ####


#### WEEK 3 ####
"""
Week 3

day 1:- Functions Basics ✔
day 2:- Advanced Functions ❌
day 3:- Classes and Objects ❌
day 4:- Inheritance & Polymorphism ❌
    day 5:- Library Management System ❌

"""
####    ####


#### WEEK 4 ####
"""
Week 4

day 1:- File Operations ❌
day 2:- Error Handling ❌
day 3:- Virtual Environment & Packaging ❌
day 4:- Popular Libraries ❌
    day 5:- File Based Track Manager ❌

"""
####    ####


#### WEEK 5 ####
"""
Week 5

day 1:- Database Integration ❌
day 2:- Testing & Debugging  (Work in Progress)❌
day 3:- API Integration ❌
day 4:- Project Integration ❌
    day 5:- Personal Fitness Tracker ❌

"""
####    ####


###### We can create a Student personal manager System :- We can give options like Grade Calculator/Student Grade Manager, Library management system ,
# Student health manager/personal fitness Tracker, Student files tracker/storage system

student = input("Enter Your name: ").capitalize()
def Student():
    print(f"Hello {student},I'm Jarvis your personal Manager 💻.")
   

    while True:
            # print("")
        def Grades():
            print("Hello, ",student)
            grades = []
            # num_sub = int(input("Enetr the number of subjects"))
            num_sub = 4
            print("Subjects: Maths,Hindi,English,Science")
            for i in range(num_sub):
                elements = int(input(f"Enter the marks for each Subject: "))
                # ts = elements.split() 
                grades.append(elements)

            def Grade_Manager():
                print("Grade Manager:")
                print("Your marks:")
                print("Maths:",grades[0]) 
                print("Hindi:",grades[1]) 
                print("English:",grades[2]) 
                print("Science:",grades[3]) 


            def Grade_Calculator():

                    print("Grade Calculator")
                    num_sub = 4
                    total_grades = sum(grades)/num_sub 
                    # print("Your marks:",grades)
                    avg_mrks = sum(grades) / num_sub
                    highest = max(grades)
                    lowest = min(grades)
                    if total_grades >= 90:
                        print("A - distinction")
                        print("Hello "+ student + " Your Highest marks are:",highest)

                    elif total_grades >= 80:
                        print("B - Grade")
                        print("Hello"+ student + "Your Highest marks are:",highest)

                    elif total_grades >= 70:
                        print("C Grade ")
                        print("Hello"+ student + "Your Average marks are:",avg_mrks)

                    elif total_grades >= 50:
                        print("D Grade ")
                        print("Hello"+ student + "Your Lowest marks are:",lowest)

                    else:
                        print("F-Fail")


            print("What would you like to do:\n 1.Manage Grades \n 2.Calculate Grades")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                 Grade_Manager()
            elif choice == 2:
                 Grade_Calculator()
            else:
                 print("Enter valid option:")

        def Fitness_Tracker():
            print("")

        def File_Tracker():
            print("")
        break
    

    print("I can help you manage things like: \n1.Grade Management \n2.Health/Fitness Manager \n3.Library/books Management \n4.File Tracker/Storage.")
    while True:
        choice = input("Please select a option from 1,2,3,4 :")
        if choice == "1":
            print("Welcome to your personal Grade Management System.")
            Grades()
            break
        elif choice == "2":
            Fitness_Tracker()        
            print(f"Hello {student},I'm Fitness Tracker 😁")
            break
        elif choice == "3":
            print("")
            File_Tracker()
            print("Hey we are here to Track/Manage/Store your files.")
            break
        
        elif choice == "4":
            print("")
            break
        else:
             print("Please choose a valid option. ")

Student()