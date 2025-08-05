<<<<<<< HEAD
# LIST 
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

"""
mylist = ["kiwi","apple","mango","apple"]
print(mylist)
print(len(mylist))

"""

"""
my1 = ["kiwi",10,3.5,True]
print(type(my1))


thislist = (("apple","kiwi","mango")) # using the  list constructor -> done by using double brackets (())
print(thislist)

"""


# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

'''
thislist = ["kiwi","mango",10]
print(thislist[2])
print(thislist[-2])
'''

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items

# By leaving out the start value, the range will start at the first item: //By leaving out the end value, the range will go on to the end of the list:
# print(thislist[:4])//print(thislist[2:])
'''
listt = ["new",True,"demo",45,78,87,"hey"] 
print(listt[2:5])
print(listt[:4])
print(listt[2:])

'''

'''
mylist = [5,45,22,"22"]
index = mylist.index(22)
if 2 in mylist:
    print("yes 22 do exists in the list")
    print(f"it exists at index {index}")
else:
    print("No it doesn't exists  in the list")

'''

# mylist = ["kiwi",20,"apple",True]
# print(mylist)


'''
mylist[2] = 10
print(mylist)

mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)
mylist[1:2] = ["blackcurrant", "watermelon"]
print(mylist)
list.insert(2, "watermelon")
print(mylist)


thislist = ["apple", "banana", "cherry"] #The clear() method empties the list. The list still remains, but it has no content.
thislist.clear()
print(thislist)

'''

'''

for x in mylist:
    print(x)

for i in range(len(mylist)):
    print(mylist[i])

i = 0
while i <len(mylist):
    print(mylist[i])
    i = i + 1

for x in mylist:
    print(x)

[print(x) for x in mylist]

'''

'''
fruits = ["kiwi","apple","mango"]
thislist = []

for x in fruits:
    if "a" in x:
        thislist.append(x)
print(thislist)


newlist = [x for x in fruits if "a" in x]

print(newlist)

'''





# TUPLES
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

"""
thistuple = ("apple","kiwi","cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

mytuple = tuple(("apple","kiwi","mango"))
print(type(mytuple))

"""
# Change Tuple Values:- Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

"""
x = ("apple","mango","kiwi") # here we take a tuple 

y = list(x) # then we convert it into the list and then changed the value/element  
y[1] = "kiwi"
y.append("orange")
y.remove("apple")

x = tuple(y) # then we converted the list back into tuple 
print(x)
thistuple = ("mango","apple","kiwi")
y = ("orange",)
thistuple += y
print(thistuple)

del thistuple
print(thistuple)# this will give the error that  "thistuple" doesnt exists because we already have deleted it 

"""



"""
fruits = ("kiwi","orange","cherry")

(green,red,blue) = fruits

print(green)
print(red)
print(blue) 

# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:
#############            a          =       (45,"hey")        #############
#############        variables                values          #############


fruits1 = ("kiwi","orange","cherry","apple","apple","apple")

(green,*red,blue,black) = fruits1

print(green)
print(red)
print(blue)
print(black)

"""



"""

thistuple = ("kiwi","orange","cherry")

for x in thistuple:
    print(x)



for i in range(len(thistuple)):
    print(thistuple[i])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


for x in ("hey","hello","hiii"):
    print(x)

thistuple = ("kiwi","orange","cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

"""

"""
tuple1 = ("hey","hello","hey")
tuple2 = ("HIIII",)

tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 2
print(tuple4)

"""



# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

"""tuple1 = ("hey","hello","hey")
tuple3 = tuple1.count("hey")
tuple4 = tuple1.index('hey')
print(tuple3)
print(tuple4)
"""





=======
mylist = ["banna","apple","kiwi"]
print(len(mylist))
>>>>>>> main
