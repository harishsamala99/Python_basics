def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = divide(a, b)
except ValueError as e:
    print("Error:", e)
else:
    print(f"The result is {result}")
finally:
    print("Done")
