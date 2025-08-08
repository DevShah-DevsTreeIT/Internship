# Car Dealership :- Create Car and Dealership classes with inventory management
# Available cars,Sell car,

class Car:
    def __init__(self , cname , model , year, price ):
        self.cname = cname
        self.model = model
        self.year = year
        self.price = price
 
    def car_details(self):
        return f"{self.cname}  {self.model}  {self.year} {self.price}"
 
class Dealership:
    def __init__(self , name ):
            self.name = name
            self.inventory = []

    def car_display(self):
        if self.inventory:
            print(f"######### Welcome to the Inventory of {self.name} ############")
            for car in self.inventory:
                print(car.car_details())
            print(f"Thanks, Visit again 😁")
        else:
            print('\n')
            print("Inventory is empty")

    def add_car(self , cname , model , year , price):
         car = Car(cname , model , year , price)
         self.inventory.append(car)
         print("Added in Inventory")
         print('\n')
 
   
car_name = input("Car Name :")
car_model = input("Car Model :")
car_year = input("Car Year :")
car_price = input("Car Price :")
 
c2 = Dealership("Carwale")
 
c2.add_car(car_name , car_model , car_year , car_price)
c2.car_display()