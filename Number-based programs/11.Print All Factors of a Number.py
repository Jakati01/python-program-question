num = int(input('Enter the num:'))
if num ==0:
    print('Please enter the postive num')
else:
    for i in range(1,num+1):
        if num %i==0:
            print(i,end=' ')