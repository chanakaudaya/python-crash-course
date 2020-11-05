prompt = "\n Please enter a name of a city you have visited."
prompt += "\n Enter 'quit' when you are finished. "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"Nice!. I have visited {message} too.")