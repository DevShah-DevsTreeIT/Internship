# Number Guessing Game
import random


default_num = random.randint(1,100)
while True:
    number = int(input("Enter a number"))

    if number == default_num:
        print("Yup, you got it right")
      
        choice  = input("Want to  restart Y or N: ").lower()
        if choice == "y":
            continue
        else:
            break
    elif number < default_num:
        print("It's lower than the number,Try again")
    elif abs(number - default_num) <= 5 : 
        print("You are Close to the number")
    elif number > default_num:
        print("It's higher than the number,Try again")
