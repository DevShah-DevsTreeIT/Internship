# w4d2-t1_Safe Calculator :- Build a calculator with comprehensive error handling for invalid inputs

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_number_input(self):
    while True:
        try:
            num = float(input(self))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_choice():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice(1/2/3/4/5): ")
        if choice in ('1', '2', '3', '4', '5'):
            return choice
        else:
            print("Invalid input. Please enter a choice from 1 to 5.")

def calculator():
    print("Welcome to the Safe Calculator ")
    while True:
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        choice = get_operation_choice()

        if choice == '5':
            print("Thanks for using our Calculator")
            break

        try:
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()