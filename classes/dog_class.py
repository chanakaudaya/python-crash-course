class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is sitting now.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog("willie",6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()
my_dog.roll_over()
