from datetime import date

# class Car_I: 
#     color = 'red'
#     # def __new__():
#     #     return 
#     def __init__(self):  # Car.__init__(car)
#         # self.color = 'black'
#         self._init()

#     def _init(self):
#         self.color = 'black'

#     def info_Class():
#         print(f"Class {__class__.__name__} has attribut color: {__class__.color}")

#  1. class Cat:
#     attrs: name, age, breed, color, position=(x, y)
#     method: 
#          info() - animal description
#          move(distance) - move animal by printing 

#  2. class Dog:
#     attrs: name, age, breed, color
#     method: 
#          info() - animal description
#          move(distance) - move animal by printing 

#  2. class Bird:
#     attrs: name, age, breed, color
#     method: 
#          info() - animal description
#          move(distance) - move animal by printing  distance=(dx, dy)


class Car:

    count = 0
    # def __new__():
    #     return 
    def __init__(self, prod_year, color, brend, category):  # Car.__init__(car, prod_year, color, brend, category)
        self.color = color
        self.prod_year = prod_year
        self.brend = brend
        self.category = category
        Car.count += 1 
        self._init()

    def _init(self):
        self.age = date.today().year - self.prod_year

    def info(self):
        print(f"Car {self.brend} of {self.prod_year} year is {self.category} and has color {self.color}")

    def info_class():
        print(f"Class {__class__.__name__} was created: {__class__.count}")

    def __del__(self):
        __class__.count -= 1
        # print(f"{__class__.__name__} removed...")


class PCar(Car):  # PKW LKW

    count = 0

    def __init__(self, prod_year, color, brend, category, place_count):
        super().__init__(prod_year, color, brend, category)
        self.place_count = place_count
        __class__.count += 1

    def info(self):
        print(f"PCar {self.brend} of {self.prod_year} year is {self.category} and has color {self.color}")
        print(f"PCar place count = {self.place_count}")

    def info_class():
        print(f"Class {__class__.__name__} was created: {__class__.count}")

    
class Truck(Car):

    count = 0

    def __init__(self, prod_year, color, brend, category, capacity):

        super().__init__(prod_year, color, brend, category)
        self.capacity = capacity
        __class__.count += 1

    def info(self):
        print(f"Truck {self.brend} of {self.prod_year} year is {self.category} and has color {self.color}")
        print(f"Truck capacity = {self.capacity}")

    def info_class():
        print(f"Class {__class__.__name__} was created: {__class__.count}")


# mro()
class A:
    def info(self):
        print(__class__.__name__)


class Ab(A):
    def info(self):
        print(__class__.__name__)
        super().info()


class Ac(A):
    def info(self):
        print(__class__.__name__)
        super().info()


class B(Ab, Ac):
    def info(self):

        print(__class__.__name__)
        super().info()



class C(Ac):
    def info(self):
        
        print(__class__.__name__)
        super().info()


class D(B, C):
    def info(self):
        
        print(__class__.__name__)
        super().info()

#     A
#   /   \
#  Ab    Ac
#   \  /  \
#    B     C
#     \   /
#       D

if __name__ == '__main__':

    PCar.info_class()
    car1 = PCar(2000, 'blue', 'Audi', 'cupe', 4) 
    car2 = PCar(2010, 'white', 'Mercedes', 'sedan', 5) 
    Car.info_class()

    print(car1.color, car2.color)

    # car2.color = 'blue'
    car1.info()
    car2.info()

    car1._init()
    print(Car.count, car1.__dict__['color'])
    # Car_I.info_Class()
    # del car1
    print(car2.count)
  

    truck1 = Truck(2000, 'blue', 'VOLVO', '', 10000)
    truck2 = Truck(2000, 'red', 'MAN', '', 10000)

    Car.info_class()
    PCar.info_class()
    Truck.info_class()

    print(D.mro())
    d = D()
    d.info()