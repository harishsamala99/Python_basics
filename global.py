

x=10
def modify_global():
    global x
    x=5
modify_global()
print(x)

def sum(a,b):
    print("hi")
    c=a+b
    return c
print(sum(2,3))

def add(a,b):
    """
    return sum of two numbers 
    a=(int): the first number
    b=(int): the second number
    
    retunrs:
    int: the sum of two number
    """
    return a+b