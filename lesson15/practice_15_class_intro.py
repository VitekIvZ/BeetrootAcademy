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
        print(f"Class {__class__.__name__} was created: {Car.count}")

    def __del__(self):
        __class__.count -= 1
        print("removed...")


if __name__ == '__main__':

    Car.info_class()
    car1 = Car(2000, 'blue', 'Audi', 'cupe') 
    car2 = Car(2010, 'white', 'Mercedes', 'sedan') 
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
    Car.info_class()
