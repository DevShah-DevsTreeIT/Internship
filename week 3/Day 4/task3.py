# Employee System:- Design Employee hierarchy with different types and polymorphic salary calculation

class Employee:
    def __init__(self,perhour = 220,hours = 0,bonus = 200):
        self.perhour =  perhour       
        self.hours = hours
        self.bonus = bonus    


class FullTimer(Employee):

    def __init__(self):
        super().__init__()

    def calculate_salary(self):
        print("Hello I'm a full time employee")
        self.hours = 9
        salary = 30 * (self.perhour * self.hours + self.bonus)
        # self.calculate_salary(salary)
        print(f"My salary is {salary}")



class PartTimer(Employee):


    def calculate_salary(self):
        print("Hello I'm a part-time employee")
        self.perhour = 62.5
        self.hours = 4
        salary = 30 * (self.perhour * self.hours)
        print(f"My salary is {salary}")



class Intern(Employee):


    def calculate_salary(self):
        print("Hello I'm a Intern")
        perday = 166.66666666666666
        workday = 30
        salary = (perday * workday)
        print(f"My salary is {salary}")
    
    
emp1 = FullTimer()
emp2 = PartTimer()
emp3 = Intern()

employees = [emp1,emp2,emp3]

for emp in employees:
    emp.calculate_salary()
