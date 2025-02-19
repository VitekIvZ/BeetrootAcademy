
#   self.speed = speed  !!!!

class Cat:

    # distance = (0, 0)

    def __init__(self, name, age, breed, color, position=(0, 0)): #
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.position = position   # Cat.distance

    def info(self):
        print(f"My cat’s name is {self.name}. It’s {self.age} year old. It’s a {self.color} {self.breed} cat.")
        # print(f'The cat is there - {self.position}')

    def move(self, distance):
        x, y = self.position
        dx, dy = distance
        self.position = (x+dx, y+dy)
        print(f"Position was changed to {self.position}")


class Dog:
    def __init__(self, name, age, breed, color, position=(1, 1)): # x, y, 
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.position = [position[0], position[1]]   # Cat.distance

    def info(self):
        print(f'The dog {self.name} is a {self.age}, {self.breed} years old, {self.color} in color.' )

    def move(self, dx, dy):  # dx, dy  distance
        # self.position[0], self.position[1] = self.position[0]+distance[0], self.position[1]+distance[1]
        if (dx, dy) != (0, 0):
            self.position[0], self.position[1] = self.position[0]+dx, self.position[1]+dy
            print(f'{self.name} was walked to position {self.position[0]}, {self.position[1]}')
        else:
            print(f'{self.name}\` position was not chanched: {self.position[0]}, {self.position[1]}')


class Bird:
    def __init__(self, name, age, breed, color, x, y):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.position = [x, y]

    def info(self):
        return f'My bird - {self.name}, she is ({self.age} years old, she have - {self.color} and {self.color} color)'
    
    def move(self, distance: list):
        self.position[0], self.position[1] = self.position[0]+distance[0], self.position[1]+distance[1]

        # self.position = distance
