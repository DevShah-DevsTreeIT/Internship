# If the file is located in a different location, you will have to specify the file path, like this:
# Open a file on a different location:-   f = open("D:\\myfiles\welcome.txt")

# f = open("demofile.txt")
# print(f.read())

# with open("demofile.txt") as f:
#     print(f.read())




# You can also use the with statement when opening a file:

# Example
# Using the with keyword:



###############
# Create a New File :- To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists


# f = open("task1.txt", "x")

# with open("task1.txt", "w") as f:
#   f.write("Hello World!")

# #open and read the file after the overwriting:
# with open("demofile.txt") as f:
#   print(f.read())




# Python File Operations Overview:- File operations in Python are commonly grouped into three main categories:
# 1. Basic File Handling
# 2. Working with Directories
# 3. Advanced File Operations




###########################   1. Basic File Handling  ###########################
# Python provides built-in functions to work with files using the open() function.


# file = open("example.txt","r")


# File Modes:
#    Mode	Meaning
#    'r'	Read (default)
#    'w'	Write (overwrites file)
#    'a'	Append
#    'x'	Create (error if exists)
#    'b'	Binary mode
#    't'	Text mode (default)
#    '+'	Read and write


# ######### reading from a file  
# f = open("example.txt","r")

# content = f.read() # this will reads the whole file 
# line = f.readline() #thiss will read only one line 
# lines = f.readlines() # returns list of lines

# f.close()
# ######### writing to a file

# f = open("example.txt","w") #this will overwrites the file 
# f.write("Hello, World\n") 
# f.writelines(["Line1\n","Line 2\n"])
# f.close()

# #  Best Practice: Use with Statement

# with open("example.txt", "r") as f:
#     content = f.read()

# The File is automatically closed :- by using the "with" statement we don't need to close it by f.close() it will get closed automatically 





###########################   2. Working with the directories   ###########################

###### we can manage file and directories using the os and shutil modules

# # here are some important need modules :- 
# import os 
# import shutil


# ###### dirctory operations 
# # Get current working directory
# print(os.getcwd())

# # Change directory
# # os.chdir("path/to/directory")

# # Create a new directory
# os.mkdir("new_folder")

# # Create multiple nested directories
# os.makedirs("folder1/folder2")

# # Remove a directory
# # os.rmdir("new_folder")              # Only if empty
# # shutil.rmtree("task1.txt")           # Deletes even if not empty

# # List files and directories
# files = os.listdir()



###########################   3. File Manipulation  ###########################


########### rename and delete files  

# Rename a file
# os.rename("demofile.txt", "task1.txt")

# # Remove a file
# os.remove("new.txt")


########### copy files and directories   

# shutil.copy("source.txt", "dest.txt")               # Copy file
# shutil.copy2("source.txt", "dest.txt")              # With metadata
# shutil.copytree("src_folder", "dest_folder")        # Copy directory


# ###########  Check File/Directory Existence

# os.path.exists("file.txt")               # True/False
# os.path.isfile("file.txt")
# os.path.isdir("folder")


# ###########################  🔹 4. usefull os.path functions  ###########################

# import os

# # Join paths safely
# path = os.path.join("folder", "file.txt")

# # Get absolute path
# os.path.abspath("file.txt")

# # Split path
# folder, file = os.path.split("/folder/file.txt")

# # Get file extension
# name, ext = os.path.splitext("file.txt")


# ############################   🔹 5. Working with Paths (Modern Alternative)  ########################### 
# ### Python 3.4+ has a powerful pathlib module.

# from pathlib import Path

# p = Path("example.txt")

# # Read and write
# content = p.read_text()
# p.write_text("New content")

# # Path operations
# print(p.exists())
# print(p.is_file())
# print(p.suffix)        # .txt
# print(p.stem)          # example




# ############################   🔹 6. reading binary files(e.g. Images .PDFs)  ########################### 


# with open("image.jpg", "rb") as f:
#     data = f.read()

# with open("copy.jpg", "wb") as f:
#     f.write(data)


# ############################   🔹 7. File Iteration (Line-by-Line)  ########################### 
# # This is a efficient way for large files:

# with open("bigfile.txt", "r") as f:
#     for line in f:
#         print(line.strip())



# ########################################🔹IMP Cheat sheet ##############################
# ################################ | Task               | Code Example                                   |
# ################################ | ------------------ | ---------------------------------------------- |
# ################################ | Read file          | `f.read()`, `f.readline()`                     |
# ################################ | Write/append       | `f.write()`, `f.writelines()`                  |
# ################################ | With statement     | `with open(...) as f:`                         |
# ################################ | List files in dir  | `os.listdir()`                                 |
# ################################ | Create directory   | `os.mkdir()`, `os.makedirs()`                  |
# ################################ | Remove file/dir    | `os.remove()`, `os.rmdir()`, `shutil.rmtree()` |
# ################################ | Copy file/dir      | `shutil.copy()`, `shutil.copytree()`           |
# ################################ | Check existence    | `os.path.exists()`                             |
################################ | Pathlib modern API | `Path("file").read_text()`                     |

