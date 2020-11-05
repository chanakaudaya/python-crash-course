def make_pizza(size, *toppings):
    """Print a summary of the pizza we are about to make."""
    print(f"\nMaking a {size} inch pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza(12, "peperroni")
make_pizza(16, "garlic", "cheese","tomatoes")
