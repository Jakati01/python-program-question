first = int(input('Enter the first num:'))
second = int(input('Enter the second num:'))
gcm =1


for i in range (1,min(first,second)):
    if first%i==0 and second %i==0:
        gcm=i
lcm = (first*second)//gcm
print(lcm)