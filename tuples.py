# creating a tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# loop through a tuple using for
for dimension in dimensions:
    print(dimension)

# change the tuple
dimensions = (400,10)
for dimension in dimensions:
    print(dimension)

# tuple with 5 dimensions
colors = ("red", "green", "blue", "yellow", "orange")
for color in colors:
    print(color)

print("\nnew colors.\n")

# Assign a new value to the tuple
colors = ("red", "black", "blue", "yellow", "purple")
for color in colors:
    print(color)
