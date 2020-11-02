requested_toppings = ['green chillie', 'mushroom','extra cheese' ]
for topping in requested_toppings:
    if topping == 'green chillie':
        print("Sorry, we are out of green chillie")
    else:
        print(f"Adding topping {topping}")
print("Pizze is prepared!")

# checking list if it is empty or not before looping through the items
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping} to the pizza")
    print("Pizza is prepared")
else:
    print("Are you sure you want a plain pizza?")

# using multiple lists
available_toppings = ['green pepper', 'mushroom', 'garlic', 'sausage', 'tomatoes', 'extra-cheese']
requested_toppings = ['mushroom', 'green chillie','tomatoes']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adding the {topping} to the pizza")
    else:
        print(f"Sorry, the {topping} is not available")
print("Pizza is ready!")