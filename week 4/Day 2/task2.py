import os
print("Welcome to the the file operation system: ")


while True:
    
    fname = input("Enter the file name: ")
    if not fname.endswith(".txt"):
        fname += ".txt"
    
    print("Enter the operation you would like to perform: ")
    print("1. Read a file")
    print("2. Write/update a file")
    print("3. Delete file")
    print("4. Rename the file")

    choice = input("Enter your choice: ")

    if choice == "1":
        try: 
            with open(fname) as file:
                print(f"The File '{fname}' is opended. ")
                content = file.read()
                print(content)
                break
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except PermissionError:
            print(f"Permission Denied/not allowed to access this file/ {e}")
        
    elif choice =="2":
        try: 
            lines = input("Enter the text you want to add in the file: \n ")
            with open(fname,"w+") as file:
                file.write(lines)
                # file.write = input("Enter the text you want to write in the file: ")
                print("The  file  is updated: ")
                file.seek(0)
                content = file.read()
                print(content) 
                break
        except PermissionError:
            print("Permission Denied/not allowed to access this file.")
        except OSError as e:
            print(f"an error occured {e}")

    elif choice == "3":
        option = input("are you sure you want to delete the file: ").lower()
        if option in ("y","yes"):
            
            try:
                # with open(fname) as file:
                os.remove(fname)
                print("Done its deleted now")
                break
            except FileNotFoundError:
                print("Cannot find the file of this name: ")
            except PermissionError:
                print("Doesn't have the access to delete the file.")

    elif choice == "4":
        nname = input("Enter the new name: ")
        if not nname.endswith(".txt"):
            nname += ".txt"        
        try:
            if os.path.exists(nname):
                print(f"File '{nname}' already exists. Choose another name.")
            else:
                os.rename(fname, nname)
                print(f"File renamed from {fname} to {nname}")
                break
        except FileNotFoundError:
            print(f"File '{fname}' not found.")
        except FileExistsError:
            print(f"A file named '{nname}' already exists.")
        except PermissionError:
            print("Permission denied to rename the file.")
 
        except OSError as e:
            print(f"Error renaming file: {e}")
    else:
        print("Please Choose a valid option.")