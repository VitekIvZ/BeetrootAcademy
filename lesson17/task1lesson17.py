#task1lesson17.py


"""
Method overloading.

Create a base class named Animal with a method called talk and then create two subclasses: 
Dog and Cat, and make their own implementation of the method talk be different. 
For instance, Dog's can be to print 'woof woof', while Cat's can be to print 'meow'.

Also, create a simple generic function, which takes as input instance of a Cat or 
Dog classes and performs talk method on input parameter.  
"""

class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def make_animal_talk(animal):
    animal.talk()


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    make_animal_talk(dog)  
    make_animal_talk(cat)  


