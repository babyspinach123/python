import winsound
# Need to 'pip install colorama' to download the colorama module
# To check it is installed use 'pip list'
# To save all modules you have installed use 'pip freeze > requirements.txt'
# To install all the modules needed do 'pip install -r requirements.txt'
from colorama import Fore,Style

def display (message , is_warning=False):
    if is_warning:
        print(f'{Fore.RED}WARNING: {Style.RESET_ALL}' + message)
    else:
        print (message)

def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)