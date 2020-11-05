def get_formatted_name(first_name, last_name):
    """ Return a full name. Nicely formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimmy","hendrix")
print(musician)
