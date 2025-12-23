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