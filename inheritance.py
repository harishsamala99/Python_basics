class Animal():
    location="Australia"
    
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print("generic animal sound")
        
class Dog(Animal):
    def speak(self):
        print("woof")
        
d=Dog("bruno")
d.speak()
print(d.location)
        
        