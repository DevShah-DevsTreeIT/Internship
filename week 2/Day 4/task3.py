# Menu-Driven Program
# Create  a menu system using loop wiht break and continue statements

name = input("Enter Your name to continue: ")
print(f"Hey {name},Welcome to our Online Store")


Avalaible_Products ={ 1:"Apple",
                       2:"Kiwi",
                       3:"Mango",
                    }
cart = []
wishlist= []

while True:
    print("\t Avalaible Options: \t")
    print("1. View all Products")
    print("2. Add Product To cart ")
    print("3. Add to Wishlist")
    print("4. View Cart")
    print("5. Remove Item from Cart/Wishlist")
    print("6. Exit")
    
    choice = input("Enter Your Choice from 1-6: ")
   
    if choice == '1':
        print(f"###---Avalaible_Products---###")
        for pid ,pname in Avalaible_Products.items():
            print(f"{pid}. {pname}") 

    elif choice == '2':
        pid = int(input("Enter the id of the Product you wants to add to Cart: "))
        if pid in Avalaible_Products:
            cart.append(Avalaible_Products[pid])
            print(f"Product {Avalaible_Products[pid]} Added To the Cart.")
        else:
            print("Invalid Product ID.")

    
    elif choice == '3':
        pid = int(input("Enter the Product you wants to add to Wishlist: "))
        if pid in Avalaible_Products:
            print(f"Product {Avalaible_Products[pid]} Added to Wishlist.")
            wishlist.append(Avalaible_Products[pid])
        elif pid in wishlist:
            print("Product already there in your Wishlist.")
        else:
            print("Invalid Product ID.")
    
    elif choice == '4':
        print("Your Cart:")
        if cart:
            for item in cart:
                print("-",item)
        else:
            print("Cart is Empty")

    
    elif choice == '5':
        choice1 = input("1.Cart, 2.Wishlist ")
        if choice1 == '1':         
            item = input("Enter product name to remove from cart: ")
            if item in cart:
                cart.remove(item)
                print(f"{item} removed from cart.")
            else:
                print("Item not in cart.")
        elif choice1 == '2':
            item = input("Enter product name to remove from wishlist: ")
            if item in wishlist:
                wishlist.remove(item)
                print(f"{item} removed from wishlist.")
            else:
                print("Item not in wishlist.")
        else:
            print("Please choose from 1.Cart or 2.Wishlist ")

    elif choice == '6':
        print(f"Thanks {name} for visiting our Store! 🛍️")
        break
    else:
        print("Invalid Choice,Please choose the option properly: ")
        continue