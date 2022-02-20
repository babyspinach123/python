from logging import exception


x = input('first number: ')
y = input('second number: ')
# x = float(x)
# y = float (y)
try:
    # print(f'first number divided by second number = {str(x/y)}')
    print(f'first number divided by second number = {float(x)/float(y)}')
except ZeroDivisionError as e:
    print(f'not allowed to divide by zero: {e}')
except Exception as e:
     print(f'something else went wrong: {e}')
finally:
    print('this is our cleanup code')
