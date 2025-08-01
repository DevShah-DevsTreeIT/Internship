# There two types of type conversion
# first one is implicit and the second one is explicit 




# implicit --> it converts data type automatically 

coffee_price = 5
donut_price = 2.5
total_price  = coffee_price + donut_price
print("Total price:",total_price)
print("Type of the total_price:",type(total_price))


num1 = 10
num2 = 2
result = num1 / num2  # Python automatically returns float
print(result)  # Output: 5.0
print(type(result))  # Output: <class 'float'>


# explicit --> it doesnt convert the data types automatically we have  to manualy convert the data types uaing functions 


age_input = "21"
age = int(age_input)


if age > 18:
    print("you are eligible to vote")
else:
    print("You aren't eligible to vote")


students = ["Alice", "Bob", "Charlie"]  # List
students_tuple = tuple(students)  # Convert to tuple
print(students_tuple)




default_categories = ("Electronics", "Clothing", "Groceries")  # Tuple
categories_list = list(default_categories)  # Convert to list
categories_list.append("Books")  # Add a new category
print(categories_list) 



products = {"Laptop": 800, "Phone": 500, "Tablet": 300}
product_names = list(products.keys())  # Extract only keys (product names)
print(product_names)  # Output: ['Laptop', 'Phone', 'Tablet']



username = input("Enter your name: ")  # User enters a name
if bool(username):  # Converts string to boolean
    print("Welcome,", username)
else:
    print("Please enter a valid name!")





# when we try to dirclty conert the age in to string it wont get converted and we will get an error in it 
# print(f"My name is"+ name + ",I'm " + age +" years old, my hobbies are "+ hobbies + " ,I'm currently pursing Btech from Silver Oak University in" + Degree)


# Traceback (most recent call last):
#   File "C:\Users\Internship\Desktop\Internship\py\week 1\Day 3\task3.py", line 8, in <module>
#     print(f"My name is"+ name + ",I'm " + age +" years old, my hobbies are "+ hobbies + " ,I'm currently pursing Btech from Silver Oak University in" + Degree)
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str

