first_name = input('what is your first name? ')
last_name = input('what is your last name? ')
print ('hello '+first_name.capitalize()+' '+last_name.capitalize())
print('hello {1}, {0}'.format(first_name.capitalize(), last_name.capitalize()))
print(f'hello {first_name.capitalize()} {last_name.upper()}')