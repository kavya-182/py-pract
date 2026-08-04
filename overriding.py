# Base class
class Animal:
    def sound(self):
        print("Animals make different sounds.")

# Derived class Dog
class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

# Derived class Cat
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

# Derived class Cow
class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")

# Demonstration of method overriding
dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()