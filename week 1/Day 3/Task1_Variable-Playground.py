## Variables
a, b, c = 5, "Hello", 3.5
print(a)  # Output: 5
print(b)  # Output: Hello
print(c)  # Output: 3.5

# Using Variables with Strings
customer_name = "Alice"
message = "Hello, " + customer_name + "! Welcome back."
print(message)


#--->> Different types of data types 

## Numeric ##

a = 10   #Integer
print( a   ,type(a))
b = 3.14 #Float
print( b   ,type(b))

current = 5 + 3j  # 5 is the real part, 3j is the imaginary part
voltage = 2 + 4j
power = current * voltage  # Complex number multiplication
print("Power in circuit:", power)
## Sequence variables ##

string = "Heyy"
print( string   ,type(string))
tuple = (1,2,3)
print( tuple   ,type(tuple))
list =  [1,2,3]
print( list   ,type(list))

## mapping variables-> This refers to objects that store data in key-value pairs,allowing for efficient retrieval of values based on their associated keys.

dictionary = {"Name":"Dev","Age":22 }
print( dictionary   ,type(dictionary))

## Set Vairables ##

set = {1,2,3,4}
print( set   ,type(set))

## frozenset -> a immutable version of set ##


## Boolean True or false ##
c = 12
d = 12

is_equal = c == d
print(is_equal   ,type(is_equal))


#  Special Variables -->> NoneType: Represents the absence of a value (e.g., None).


x = y = z = 100
print(x, y, z)