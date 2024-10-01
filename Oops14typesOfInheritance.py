#single inheritance
# class Animal:
#     def sound(self):
#         return "Animal Sound"

# class Dog(Animal):
#     def bark(self):
#         return "Woof!"

# dog = Dog()
# print(dog.sound())
# print(dog.bark())

#Multiple Inheritance
# class Mammal:
#     def fly(self):
#         print("Mammal can walk")
# class Bird:
#     def fly(self):
#         print("Bird can fly")
# class Bat(Mammal, Bird):
#     pass

# bat = Bat()
# bat.fly()   #Mammal can walk (in case of ambiguity first on will run)

#multilevel inheritance
# class Animal:
#     def sound(self):
#         return "Animal Sound"
# class Dog(Animal):
#     def bark(self):
#         return "Woof!"
# class Bulldog(Dog):
#     def breed(self):
#         return "Bulldog"
# bulldog = Bulldog()
# print(bulldog.sound())
# print(bulldog.bark())
# print(bulldog.breed())

#Hybrid Inheritance
class Engine:
    def body_type(self):
        print("Engine is a V8")
class Body:
    def body_type(self):
        print("Body is a sedan")
class Car(Engine, Body):
    pass
class ElectricCar(Car):
    def battery_type(self):
        print("Battery is Lithium-ion")
e_car = ElectricCar()
e_car.body_type() #Engine is a V8
e_car.battery_type() #Battery is Lithium-ion