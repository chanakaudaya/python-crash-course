alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(f"The alien color is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The new color of the alient is {alien_0['color']}")

# removing an item from a dictionary
print(f"The current status of the alien is {alien_0}")
del alien_0['points']
print(f"The updated status of the alient is {alien_0}")

point_value = alien_0.get('points', 'No point value is available')
print(f"Value of the alien_0 is {point_value}")

# looping through dictionaries
user_0 = {
    'first_name':'chanaka',
    'last_name':'fernando',
    'age':35,
    'favorite_language':'python'
}

for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favourite_languages = {
    'sarah':'c',
    'jen':'python',
    'jiuan':'go',
    'jin':'python'
}
for name,language in favourite_languages.items():
    print(f"\n{name.title()}'s favourite language is {language.title()}.")

# work through only the keys
for name in favourite_languages.keys():
    print(name.title())

friends = ['jiuan','jin']
for name in favourite_languages:
    print(name.title())
    if name in friends:
        print(f"Hey {name}, I see that you love {favourite_languages.get(name)}")

for language in set(favourite_languages.values()):
    print(language.title())

