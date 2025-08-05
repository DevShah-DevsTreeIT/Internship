# ageCategory Classifier 
#Child , Teen, adult , senior 

def Gender():
    print("Please select your gender:")
    print("1. Male")
    print("2. Female")
    # print("3. Non-binary")
    # print("4. Prefer not to say")

    while True:
        choice = input("Enter the number corresponding to your choice: ")
        if choice == '1':
            return "Male"
        elif choice == '2':
            return "Female"
        # break
        # elif choice == '3':
        #     gender = "Non-binary"
        #     break
        # elif choice == '4':
        #     gender = "Prefer not to say"
        #     break
        else:
            print("Invalid choice. Please try again.")

    print(f"You selected: {gender}")


def Age(age,gender):

    if age<= 12:
        print("Hey Kiddo ")
    elif age> 12 and age<= 18:
        print("Heyyy Teenager ")
    elif age> 18 and age<= 60:
        print("Welcome to the Adulthood ")
    elif age> 60 and age<= 100:
        if gender ==  "Male":
            print("Jay Shree Krishna Dada")
        else:
            print("Jay Shree Krishna Dadi")
    else:
        print("Please enter a valid age")
    


def main():
    name = input("Please enter your name: ")
    gender = Gender()

    while True:
        try:
            age = int(input("Hey, please enter your age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\n{name}, you're a {age}-year-old {gender}.")
    Age(age, gender)
    # age = input("Hey, please enter your age: ")
    # Age(age,gender)





main()
