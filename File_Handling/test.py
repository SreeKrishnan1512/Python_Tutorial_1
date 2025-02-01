class Car:

    def __init__(self,wheel):
        self.wheel=wheel

    def Wheel(self):

        print(f"The number of wheel in car is {self.wheel}")

car=Car(4)
car.Wheel()

class Vehicle(Car):

    def __init__(self,car_instance):
        self.vehicle=car_instance

    def tyre(self):
         print(f"The number of wheel in the vehicle class is {self.vehicle.wheel}")
        

vehicle=Vehicle(car)

vehicle.tyre()