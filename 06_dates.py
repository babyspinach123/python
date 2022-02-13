from datetime import datetime, timedelta, date

current_date = datetime.now()
print('today is: ' + str(current_date))

one_day = timedelta(days=1)
yesterday =current_date - one_day
print('yesterday is: ' + str(yesterday))

print('day: ' + str(current_date.day))
print('month: ' + str(current_date.month))
print('year: ' + str(current_date.year))
print('hour: ' + str(current_date.hour))
print('minute: ' + str(current_date.minute))
print('second: ' + str(current_date.second))

birthday = input('when is your birthday (dd-mm-yyyy) ')
birthday_date = datetime.strptime(birthday, '%d-%m-%Y')

time_since_birth = current_date - birthday_date
print ('days since birth: ' + str(time_since_birth.days))
