class Employee:
    company="HP"
    
    def salary(self):
        return 1200

e=Employee() #An object of class employee is created here
print(e.salary()) #Employee e's get salary method is called.
print(e.company)