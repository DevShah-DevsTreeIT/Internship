# def my_function():
#     print("Hello , Welcome to my function")

# my_function()

# def new_function(fname,lname):
#     # print(fname + " Kapoor")
#     print(fname + " " + lname)


# new_function("Ramesh","Raina")
# new_function("Ramu","")
# new_function("Suresh","khan")
# new_function("Tom","Kapoor")



# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")




# def my2_function(child3, child2, child1):
#   print("The youngest child is " + child2)

# my2_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

### https://www.w3schools.com/python/python_functions.asp

"""
def learn(name,age):
 
  set1 = {"apple","kiwi",45}
  dic1 = {"name":"HEY"}
  tuple1 =("Apple","Kiwi")  
  list1 = ["Watch","Perfume"]
  print(type(dic1))
  print(type(set1))
  print(type(tuple1))
  print(type(list1))
  print(f"my age is {age[2]} and my name is {name[2]}  ")

learn(("Jayesh","Ramesh","Suresh"),(58,54,45))
"""


# def my_fun(name="hey"):
#     print(f"Hello my nname is {name}")

# my_fun()
# my_fun("dev")



"""################### Passing a List as an Argument ###################
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# # E.g. if you send a List as an argument, it will still be a List when it reaches the function:


# def my_fun(food):
#   for x in food:
#     print(x)

# fruits = ["Kiwi","Apple","Mango"]

# my_fun(fruits)

"""

# ## return values : - to let a function returrn a value , we can use the return statement:



# def my_fun(x):
#     return x * 3
    
# print(my_fun(5))
# print(my_fun(3))


# def my_fun(x):
#   pass



# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

# Example
# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)
