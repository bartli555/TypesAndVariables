###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Bartosz'   # replace Anna with your name
surname = 'Lisowski' # replace May with your surname
full_name = name + ' ' + surname
characters_in_name = len(name)
characters_in_surname = len(surname)
characters_in_fullname =len(full_name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname}')
print(f'Your full_name has {characters_in_fullname}') # with a space between name and surname