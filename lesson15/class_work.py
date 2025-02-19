class Cat:
    distance = (0, 0)
    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        
    def info(self):
        return f"{self.name} is {self.age} age old {self.breed} and {self.color}"    
    
    def move_animal(self, x, y):
        Cat.distance = (x, y)
        return f"{self.name} moved to {Cat.distance}"
    
    
if __name__ == "__main__":
    cat1 = Cat("Tom", 5, "British", "Grey")
    print(cat1.info())
    print(cat1.move_animal(5, 10))
    

