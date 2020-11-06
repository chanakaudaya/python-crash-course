file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())
   # contents = file_object.read()

#print(contents)