
class Animal:
    def sound(self):
        print("Animals make different sounds.")
        
class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()
