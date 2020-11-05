def greet_user():
    """ Display a simple greeting."""
    print("Hello functions!")

greet_user()

def greet_user_custom(username):
    """ Display a greeting for the user."""
    print(f"Hello, {username.title()}!")

greet_user_custom("chanaka")