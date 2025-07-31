for i in range(0,20):
    print(i)
    if i==10:
        break # stops the execution of the loop at what number you mentioned.
    

class Animal:
    Location = "India"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def animal(self):
        return f"It is a {self.name} and its age is {self.age}"

# Define Tiger class OUTSIDE Animal, and inherit from Animal
class Tiger(Animal):
    def speak(self):
        return "Roarrrr"

# Create a Tiger object
t = Tiger("Tiger", 5)

print(t.name)        # Prints the tiger's name
print(t.animal())    # Uses the parent class method
print(t.Location)    # Accesses the class attribute
print(t.speak())     # Tiger speaks
