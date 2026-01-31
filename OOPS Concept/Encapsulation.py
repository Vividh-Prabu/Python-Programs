class car:
    def __init__(self,brand,wheels,airbags,mileage):
        print("This is a Constructor!!")
        self.brand=brand
        self.__wheels=wheels  # __ denotes the private variable,only accessible within the class
        self.airbags=airbags
        self.mileage = mileage

    def __del__(self):
        print("This is a Destructor!!", self)

    def __str__(self):
        return(self.brand)

    def moveforward(self,speed):
        print("Car is moving with a speed of",speed)

    def movebackward(self,speed):
        print("Car is moving with a speed of",speed)

    # Getter
    def get_wheels(self): # To print the private variable outside the class we use "getter" function
        print("No of wheels:",self.__wheels)

    # Setter
    def set_wheels(self,no_of_wheels): # To change the value of private variable outside the class we use "setter" function
        self.__wheels = no_of_wheels

print("~~~~~ Car 1 ~~~~~")
car1 = car("BMW",4,8,10.7)
print("No of wheels:",car1.get_wheels())
print("No of airbags:",car1.airbags)
print("Mileage:",car1.mileage)

# print("\n~~~~~ Car 2 ~~~~~")
# car2 = car("Mclaren",4,7,8.3)
# print("Car Name:",car2.brand)
# print("No of wheels:",car2.get_wheels())
# print("No of airbags:",car2.airbags)
# print("Mileage:",car2.mileage)


car1.set_wheels(9) 
print(car1.get_wheels()) # If we try to change the private value,it will not be reflected in the original value