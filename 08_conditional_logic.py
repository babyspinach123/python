price = input('how much did you pay? ')
price = float(price)
if price >=1.00:
    province = input('what province are you in? ')
    if province.lower() in ('alberta',\
                    'nunavut','yukon'):
        tax = 0.05
    elif province == 'ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0
print('tax rate is: ' + str(tax))

