# your code goes here!
import time

def countdown(number):
    for i in range(number):
        print(f'{number - i} SECOND(S)!')
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(number):
    for i in range(number):

        print(f'{number - i} SECOND(S)!')
        time.sleep(1)
    print('HAPPY NEW YEAR!')
