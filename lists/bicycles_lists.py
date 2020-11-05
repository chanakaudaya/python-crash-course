bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del(motorcycles[2])
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('bajaj')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


