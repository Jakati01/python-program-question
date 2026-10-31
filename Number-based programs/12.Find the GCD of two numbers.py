first = int(input('Enter the first num:'))
second = int(input('Enter the second num:'))
gcd = 1

for i in range(1,min(first,second)+1):
    if first % i==0 and second %i == 0:
        gcd=i
print(gcd)
        

    