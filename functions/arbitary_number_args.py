def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza("peperroni")
make_pizza("garlic", "cheese","tomatoes")
