def print_models(unprinted_designs, completed_models):
    """Simulating printing each design, until none is left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['jay z', 'beyonce', 'deedat']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)