age = 5
if age < 4:
    print("Your ticket fee is $0")
elif age <= 18:
    print("Your ticket fee is $25")
else:
    print("Your ticket fee is $40")

# improved version
age = 70
if age < 4:
    price = 0
elif age <= 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your ticket fee is ${price}")