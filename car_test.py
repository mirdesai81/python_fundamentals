from car import Car,ElectricCar

car = Car('hyundai','genesis','2017')
car.print_car()

tesla = ElectricCar('Tesla','Model S','2017')
tesla.print_car()
tesla.battery.print_battery()
tesla.battery.get_range()