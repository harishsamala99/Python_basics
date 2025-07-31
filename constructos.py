class Employee:
    def __init__(self,name,salary,age,bond):
        self.salary=salary
        self.name=name
        self.age=age
        self.bond=bond
    
    def salary(self):
        return self.salary
    
    def info(self):
       return f"The employee name is {self.name} and the age is {self.age} and the bond is for {self.bond} years, salary of the employee is {self.salary}" # adding return doesn't show none on the terminal but it shows when you add print statement.
        
e=Employee("kabali",1200, 26, 2)
print(e.salary)
print(e.info()) # when you the print statement in place of return you need to remove the print for print(e.info())insted just use e.info(). use print statement to get output for "return" else just enter e.info() if you use print statement.
    