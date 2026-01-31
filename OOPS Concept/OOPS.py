class car:
    def __init__(self,carbrand,no_of_wheels,no_of_airbags,mileage): # Constructor
        print("This is a constructor!")
        self.no_of_wheels = no_of_wheels
        self.no_of_airbags = no_of_airbags
        self.mileage = mileage
        self.carbrand = carbrand

    def __del__(self): # Destructor
        print("This is a destructor!",self)

    def moveforward(self,speed):
        print("Car is moving with a speed of ",speed)
    def movebackward(self):
        print("Car is moving backward")
    def __str__(self): # Removing the #(hash) code and printing the object
        return (self.carbrand)


print("~~~~~ Car 1 ~~~~~")
car1 = car("Lexus",4,6,19.7) #object creation - instance of the class - Instantiation
print("Car Name:",car1.carbrand)
print("No of wheels:",car1.no_of_wheels)
print("No of airbags:",car1.no_of_airbags)
print("Mileage:",car1.mileage)

print("\n~~~~~ Car 2 ~~~~~")
car2 = car("Bently",5,10,24.3) #object creation - instance of the class - Instantiation
print("Car Name:",car2.carbrand)
print("No of wheels:",car2.no_of_wheels)
print("No of airbags:",car2.no_of_airbags)
print("Mileage:",car2.mileage)
