class Animal():
    Location="India"
    
    def __init__(self, name,age):
        self.name=name
        self.age=age
        
    def animal(self):
        return f"it is a {self.name} and its age is {self.age}"
    
class tiger(Animal):
    def speaks(self):
        return "roarrrr"

t=tiger("tiger", 5)

print(t.name)
print(t.animal())
print(t.Location)
print(t.speaks())