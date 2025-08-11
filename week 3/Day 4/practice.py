class person:

    def __init__(self,fname,lname):
         self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(f"First name:{self.fname} and last name: {self.lname}")


class Student(person):
    
    def tp(self):
        print(f"{self.fname}  {self.lname}")

    pass

x = Student("John","Cena")

x.tp()
x.printname()

# 
# 
# 
# 