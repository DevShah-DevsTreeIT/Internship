#Higher-Order Functions

# Some basic functions to use
def square(x):
    return x * x

def double(x):
    return x * 2

def negate(x):
    return -x

#This are Higher-order function that takes another function as a parameter
def apply_function(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

numbers = [1, 2, 3, 4, 5]

# Using the higher-order function with different functions
squared_numbers = apply_function(square, numbers)
doubled_numbers = apply_function(double, numbers)
negated_numbers = apply_function(negate, numbers)
tripled_numbers = apply_function(lambda x: x * 3, numbers) 

# Output the results
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
print("Doubled numbers:", doubled_numbers)
print("Negated numbers:", negated_numbers)
print("Tripled numbers (lambda):", tripled_numbers)