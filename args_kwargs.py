#**kwargs allows a function to accept any number of keyword arguments(named arguments) and the double ** makes it works
def info(**details):
    print("User Profile: ")
    for key, value in details.items():
        print( f"{key}: {value}")
info(Name="Harish", Age=26, Country="India")

#*args allows a function to accept any number of positional arguments single* makes it work, there is no need to mention "args" we can use any other name.
def sum_numbers(*numbers):
    total=sum(numbers)
    print(f"sum : {total}")
    
sum_numbers(2,18,99)

def find_max(*values):
    print(f"max_values : {max(values)}") # mentioning the max inside {max(values)} prints out the max value.
    
find_max(55,88,19)

#using both *args and **kwargs
def show_details(a, *args, **kwargs):
    print(f"first_argument:{a}")
    print(f"Additional_positional_arguments: {args}")
    print(f"keyword_arguments: {kwargs}")

show_details(1,2,3,4, name= "Harish", Age=26)

