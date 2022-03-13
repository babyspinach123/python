from datetime import datetime

def multiply(numb1,numb2):
    result = numb1 * numb2
    return result

def print_time(message):
    print(message)
    print(datetime.now())
    print()

def get_initial(name , force_uppercase = True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial=name[0:1] 
    return initial


print_time('start of program ')
print(multiply(7,3))
first_name = input('Enter first name: ')
last_name = input('Enter Last Name: ')
print('Your initials are: ' + get_initial(first_name) + get_initial(force_uppercase= False,name=last_name))
print_time('end of program ')