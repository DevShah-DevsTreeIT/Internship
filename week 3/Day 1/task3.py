# Fibbonaci series

# Factorial: 

# n factorial  =  n!

# def fact(n):

#     result = 1
#     for i in range(2,n + 1):
#         result *= i

#     return result

# num = 5


# print(f"Factorial of", num,"is" ,fact(num))


# while True:
#     choice = input("What you wanna do?... 1.Factorial or 2.Fibonnaci")

#     if choice  == 1:
#         fact()
#     elif choice == 2:
#         fib()

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

while True:
    print("\nChoose an option:")
    print("1. Factorial")
    print("2. Fibonacci")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        num = int(input("Enter a number for factorial: "))
        print(f"Factorial of {num} is {fact(num)}")

    elif choice == "2":
        num = int(input("Enter how many Fibonacci numbers to print: "))
        print("Fibonacci series:")
        for i in range(num):
            print(fib(i), end=" ")

    elif choice == "3":
        print("Thanks for using our program.")
        break

    else:
        print("Invalid choice. Please try again.")
