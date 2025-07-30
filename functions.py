def greet(name="Harish"):
    return f"Hello, {name}"
print(greet())

def average(a,b,c):
    total=(a+b+c)/3.0
    #print(total) 
    # #or
    return total
o1=average(3,6,9)
o2=average(4,5,6)
print(o1)
print(o2)

def add(a,b):
    return a+b
print(add(5,3))

def student(name="harish", age=26):
    return f"{name}, {age}"
print(student())

def student(name="Harish",age=26,country="India"):
    return f"hi iam {name} and im {age} im from {country}"
print(student())