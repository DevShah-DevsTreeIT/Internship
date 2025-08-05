print("Welcome to the Phonebook")
phonebook = {}
while True:
    print("Please choose one of the following functions you wants to perform")
    print("1. Add a Contact")
    print("2. Remove a Contact")
    print("3. Display all Contacts")
    print("4. Search for a Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("enter name: ")
        number = input("enter Phone number: ")
        phonebook[name] = number
        print("\nThe contact added succesfullly\n")
    elif choice == "2":
        name=input("\nEnter the name of the contact you want to remove: ")
        if name in phonebook:
            del phonebook[name]
            print("\ncontact deletd successfully\n")
        else:
            print("\nThe contact doesnt exists\n ")
    elif choice == "3":
        if not phonebook:
            print("\nThe phonebook  is empty\n")
        else:
            print("\nAll Contact: ")
            for name,number in phonebook.items():
                print(f"{name} : {number}\n")  
    elif choice == "4":
        name = input("\nEnter the name of the contact you want to search: ")
        if name in phonebook:
            print(f"\nFound: {name} : {phonebook[name]}\n")
        else:
            print("\nContact not found.\n")
    elif choice == '5':
        print("Thank you for using our phonebook.")
        break
    else:
        print("\nInvalid Choise Please chooose a valid option: ")
    continue
