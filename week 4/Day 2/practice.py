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

x = 15
if not type(x) is int:


  raise TypeError("Only integers are allowed")