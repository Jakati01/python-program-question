num = int(input('ENTER THE NUM:'))
a = 0
b = 1


for _ in range(num):
    print(a,end=' ')
    a,b=b,a+b