def info(**details):
    for key, value in details.items():
        print( f"{key}: {value}")
info(name="harish", age=26, country="india")