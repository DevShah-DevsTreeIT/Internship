# Dictionary: Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, 
#Changeable: Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.


"""
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2025 #Dictionaries cannot have two items with the same key:
}

print(car)
print(car["brand"])
print(len(car))

"""

# # String, int, boolean, and list data types:

# car = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(car)
# print(type(car))



# # Using the dict() method to make a dictionary:

# car = dict(name = "John", age = 36, country = "Norway")
# print(car)



car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
#  keys : values
}

"""
x = car["brand"]
print(x)
x = car.get("model")
print(x)
x = car.keys()
print(x)
x = car["brand"]

x = car.keys()
print(car)
print(x)

car["color"] = "white"
print(car)
print(x)


x = car.values()
print(x)
car["year"] = 2020
print(x)

"""

"""
car.update({"year": 2020})
car["color"] = "red"
print(car)

x = car.items() #Get a list of the key:value pairs
print(x)

if "model" in car:
    print("It is there in the list")
else:
    print("it isnt there in the list ")

del car["year"]


car.update({"color":"blue"})
print(car)

car.pop("model")
print(car)

car.popitem()
print(car)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print(car)

del car
print(car)
"""

# thisdict = {
#     "Brand": "Ford",
#     "color": "red",

            # }
# for x in thisdict:
#     print(x)  #this will print keys in the dict
#     print(thisdict[x]) #only print the values in it

# for x in thisdict.values():
#   print(x)

# for x in thisdict.keys():
#   print(x)

# for x,y in thisdict.items():
#     print(x,y)


# myfamily = { #dict that contains three dict 
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }




# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }


# print(myfamily["child2"]["name"])



# for x, obj in myfamily.items():
#   print(x)

#   for y in obj:
#     print(y + ':', obj[y])


set1 = {'apple','kiwi','mango'}
print(set1)
print(len(set1))
print(type(set1))

'orange' in set1

set2 = set()
print(type(set2))

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6,85}


# Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)  # or set_a ^ set_b
print(f"Symmetric Difference: {symmetric_difference_set}")

# In-place update
set_c = {1, 2, 7}
set_c.update({3, 7, 8})
print(f"Updated set_c: {set_c}")