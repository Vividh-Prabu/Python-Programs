# Inheritance is a method used to reuse the code without coding a same set of codes again and again

class Vehicle: # Parent class
    wheels = 4

    def moveforward(self):
        print("Vehicle is moving forward!")

class Car(Vehicle): # Child class
    airbags = 8

class Honda(Car):
    mileage = 25.0

class Toyota(Car):
    mileage = 30.0

class Toyda(Honda,Toyota):
    has_touchscreen = True


car1 = Toyda()
print("Airbags:",car1.airbags)
print("Wheels:",car1.wheels)
print("Mileage:",car1.mileage)
car1.moveforward()

# class Father:
#     hair_color = "White"
# class Mother:
#     eye_color = "Blue"
#     hair_color = "Black"
# class Child(Father,Mother):
#     legs = 2
# child = Child()
# print(child.legs)
# print(child.hair_color)
# print(child.eye_color)