for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,20,2))
print(even_numbers)

squares = []
for value in range (1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = list(range(1,11))
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehension examples
squares = [value ** 2 for value in range (1,11)]
print(squares)

million = list(range(1,1_000_001))
print(max(million))
print(sum(million))
