'''''''''''''''
Check whether a number is divisible by 5 and 11.
'''''''''

num = int(input('ENTER THE NUMBER : '))

if num %5 ==0 and num %11 ==0:
    print(f'{num} is divisble by 5 and 11')

elif num %5 ==0:
    print(f'{num} is divisble by 5')

elif num%11 ==0:
    print(f'{num} is divisble by 11')
    
else:
    print(f'The given {num} is Not divisible by 5 and 11')