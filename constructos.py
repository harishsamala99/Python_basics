class Employee:
    def __init__(self,name,salary,age,bond):
        self.salary=salary
        self.name=name
        self.age=age
        self.bond=bond
    
    def salary(self):
        return self.salary
    
    def info(self):
        print(f"The employee name is {self.name} and the age is {self.age} and the bond is for {self.bond} years, salary of the employee is {self.salary}")
        
e=Employee("kabali",1200, 26, 2)
print(e.salary)
e.info()
    