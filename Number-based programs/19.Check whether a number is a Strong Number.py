num = int(input('ENTER THE NUM:'))


orignal = num
total =0

while num>0:
    digit = num%10
    factorial =1

    for i in range(1,digit+1):
         factorial *=i

    total +=factorial
    num =num//10
if orignal == total:
     print('It is Strong Number')
else:
     print('It is Not Strong Number')