class Person:
    def __init__(self):
        self._age = 0

    def set_age(self, age):
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным")
        else:
            self._age = age

    def get_age(self):
        return self._age

p = Person()
p.set_age(25)
print(p.get_age())
p.set_age(-5)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")


print(dog.name, dog.speak())
print(cat.name, cat.speak())


class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))



