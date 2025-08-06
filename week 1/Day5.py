# Personal Calculator with Git

print("This is your personal Calculator")

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))

Add = num1 + num2
Sub = num1 - num2
Mul = num1 * num2
Div = num1 / num2


print("Which operation you would like to perform:")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")



choice = int(input("Enter Your choice: "))
if choice == 1:
    print(f"Addition of {num1} and {num2} is: {Add}")
elif choice == 2:
    print(f"Substraction of {num1} and {num2} is: {Sub}")
elif choice == 1:
    print(f"Multiplication of {num1} and {num2} is: {Mul}")
elif choice == 1:
    print(f"Division of {num1} and {num2} is: {Div}")
else:
    print("Please Enter `a valid choice")
