class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def getMake(self):
        return self.make

    def setMake(self,make):
        self.make = make

    def print_car(self):
        print("I bought car make=" + self.make + ", model=" + self.model + ", year=" + self.year)


class Battery():

    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def print_battery(self):
        print("Battery size is " + str(self.battery_size) + " kwh.")

    def get_range(self):
        if self.battery_size == 70:
            range = 270
        else:
            range = 220
        message = "This car can go " + str(range) + " miles on a full charge."
        print(message)


class ElectricCar(Car):

    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

