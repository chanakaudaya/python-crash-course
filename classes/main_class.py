from car import Car

my_new_car = Car("audi","a4","2020")
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying attributes directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying attributes via a method
my_new_car.update_odometer(12)
my_new_car.read_odometer()

# Change attribute via addition
my_new_car.increment_odometer(200)
my_new_car.read_odometer()