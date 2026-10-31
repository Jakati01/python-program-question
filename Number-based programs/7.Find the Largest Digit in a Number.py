num = int(input("Enter a number: "))

num=abs(num)
largest = 0

while num>0:
        digit = num%10
        if largest <digit:
            largest =  digit
        num =  num//10
print(largest)