import car
import battery

class ElectricCar(car.Car):
    """Represents aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = battery.Battery()
        #self.battery_size = 75

my_tesla = ElectricCar("tesla","S","2018")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
#my_tesla.describe_battery()