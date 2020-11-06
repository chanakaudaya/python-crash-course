try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero.")

print("Enter two numbers. I'll give you the result of the division.")
print("Enter 'q' to exit.")

while True:
    first_number = input("\nFirst Number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by Zero.")
    else:
        print(answer)