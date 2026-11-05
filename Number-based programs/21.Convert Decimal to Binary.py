num = int(input('Enter the NUM: '))
if num <0:
    print('Please Enter postive Number')
binary_number=''
if num ==0:
    binary_number = 0
else:
    while num>0:
        remainder = num%2

        binary_number = str(remainder) +binary_number
        num =  num//2
print(binary_number)