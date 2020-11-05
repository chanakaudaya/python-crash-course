def describe_pet(pet_name, animal_type="dog"):
    """ Display information about a pet!"""
    print(f"\n I have a {animal_type.title()}")
    print(f" My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet("Jack")

# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to continue
# interpreting positional arguments correctly