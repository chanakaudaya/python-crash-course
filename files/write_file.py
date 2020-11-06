filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love python programming.\n")
    file_object.write("I love creating games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also like analyzing large data sets.\n")