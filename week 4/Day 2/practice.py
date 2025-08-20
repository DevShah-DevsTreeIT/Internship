import os

# Try , Except
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# try:
#   print(x)
# except:
#   print("An exception occurred")

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# try:
#   f = open("demofile.txt","w")
#   try:
#     f.write("Jay kant sikhre")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# x = 15
# if not type(x) is int:


#   raise TypeError("Only integers are allowed")



# try:
#   print(z)
# except:
#   print("something went wrong")
# finally:
#   print("The  'try except' is finished ")



# file operator with  error handling  

try:
  f = open("demofipe.txt")
  try:
    f.write("mmessage updated successfuly ")
  except :
    print("somethign went wrong when wwriting to a file")
  finally:
    f.close()
except:
  print("Something went wrong when opening a file")
finally:
  print("")

# print("Welcome to the file system:- This is a file operations with error handling")



# reading a file 
try:
  f = open("demo.txt")
except:
  print("Error: File not Found")

# For permission error 
try:
  f = open("demofile.txt")
except PermissionError:
  print("Permssion denied to access this file.")


# Writing  a file 


try:
    # Attempting to open a non-existent file in read mode
    with open("demofile.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e: # FileNotFoundError is a subclass of OSError
    print(f"Error: {e}")
except OSError as e:
    print(f"An unexpected OS error occurred: {e}")




