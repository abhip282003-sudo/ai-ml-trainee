#Implement multilevel inheritance using Animal, Mammal, and Dog classes.
class Animal:
    def dogi(self):
        print("dog can bow")
class Mammal(Animal):
    def walk(self):
        print("mammal can walk")
class dog(Mammal):
    def eat(self):
        print("dog can eat")

d=dog()
d.dogi()
d.walk()
d.eat()
