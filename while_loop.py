message = input("Tell me something and I will repeat that back to you: ")
print(message)

prompt = "Type in a number and I will tell you whether it is even or odd number."
prompt += "\n Number: "
number = input(prompt)

value = int(number)
if value % 2 == 0:
    print("The number you entered is an even number.")
else:
    print("The number you entered is an odd number.")

# using a while loop to run the program continously until user type 'quit'
prompt = "\n Tell me something, and I will repeat it back to you."
prompt += "\n Enter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

