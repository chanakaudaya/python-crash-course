cars = ['audi', 'bmw', 'toyota', 'subaru']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

requested_topping = "mushrooms"
if requested_topping != "tomatoes":
    print("Wait for tomatoes later!")

lower_limit = 18
upper_limit = 30
age_0 = 35
age_1 = 25
contestants = [age_0, age_1]

for contestant in contestants:
    if contestant >= lower_limit and contestant <= upper_limit:
        print(f"You are eligible with the age: {contestant}")
    else:
        print(f"You are not eligible with the age: {contestant}")

age_0 = 20
age_1 = 55
if age_0 > 15 or age_1 < 35:
    print(f"Both of you folks are accepted with the ages {age_0} and {age_1}")

requested_toppings = ['mushroom','tomatoes','cheese','peperoni']
if 'mushroom' in requested_toppings:
    print("You got mushroom!")

if 'chillie' in requested_toppings:
    print("You got chillie!")
else:
    print("Sorry, we don't have chillie yet!")

banned_users = ['andrew', 'nick', 'rohit']
user = 'mary'
if user not in banned_users:
    print(f"Welcome {user}!. You can access the system now!")

age = 25
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote?")
else:
    print("You are too young to vote.")
    print("Once you are 18, come back again.")
