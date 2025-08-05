# Shopping List Manager :- Create a program to add, remove, and display items in a shopping list

shooping_list = ["shirt",45,"pant"]
print(shooping_list)

# to add items in a list 

shooping_list.insert(3,"boots")
print(shooping_list)

# to remove items in a list 
del shooping_list[2]
print(shooping_list)

shooping_list.remove("boots")
print(shooping_list)


# to display items in a list 
for x in shooping_list:
    print(x)
