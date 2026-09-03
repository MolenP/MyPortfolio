class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is", self.name, "\nI'm", self.age, "years old")
    def increase_age(self):
        self.age += 1

Maxim = Person("Maxim", 16)
Arystan = Person("Arystan", 18)

Maxim.increase_age()
Arystan.increase_age()

Maxim.introduce()
Arystan.introduce()