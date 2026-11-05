num =int(input('ENTER THE NUM : '))
total =0
orignal =num

while num>0:
    digit = num%10
    total +=digit
    num = num//10
if orignal%total==0:
     print('Harshad Number')
else:
     print('not a Harshad Number')