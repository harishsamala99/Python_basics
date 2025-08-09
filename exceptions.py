def divide(a,b):
    if b==0:
        raise ValueError("Can't divide it by 0")
    return a/b
try: 
    a=int(input("Enter the number: "))
    b=int(input("Enter the number: "))
    result=divide(a,b)
except ValueError as e:
    print("Error:", e)
else:
    print(f" The result is {result}")
finally:
    print("Finished")