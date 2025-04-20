'''Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).'''

class Car:
    def __init__(self, name, color, fuel=200):
        self.name = name
        self.__model = "model"  # Default value
        self.color = color
        self.fuel = fuel

    def drive(self):
        if self.fuel <= 100 and self.fuel > 50:
            self.fuel -= 50
            print("You are running low on fuel⛽")
        elif self.fuel <= 50 and self.fuel > 0:
            print(f"You have {self.fuel}l of fuel left")
        elif self.fuel <= 0:
            print("You ran out of fuel⛽")
        else:
            self.fuel -= 50
            print("The car is moving")

    def stop(self):
        print("The car has stopped")

    def status(self):
        print(f"Fuel left: {self.fuel}")


my_car = Car("BMW", "Blue")
my_car.drive()
my_car.drive()
my_car.drive()
my_car.status()


class Truck(Car):
    def __init__(self, name, color, fuel=200, make="Make"):
        super().__init__(name, color, fuel)
        self.__make = make

    def drive(self):
        if self.fuel > 0:
            print("The truck is hauling goods")
            self.fuel -= 30
        else:
            print("The truck is out of fuel")

my_truck= Truck("Ford", "Red")
my_truck.drive()