num = input('ENTER THE OPERATOR : +,-,*, /,% : ')
OPERATOR = '+,-,*, /,%'
if num in OPERATOR:
    print (f'{num} is accepted' )
else :
    print(f'{num} is not accepted')

numA = int(input('ENTER THE FIRST NUMBER :'))
numB = int(input('ENTER THE SECOND NUMBER :'))

if num in '+':
    print(numA + numB)

elif num in '-':
    print(numA - numB)

elif num in '*':
    print(numA * numB)

elif num in '/':
    print(numA / numB)

elif num in '%':
    print('numA % numB')

print('THANK FOR USING')
