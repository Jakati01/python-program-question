num = int(input('ENTER THE NUM:'))
sign = -1 if num < 0 else 1
num =abs(num)
reverse=0

while num>0:
    digit = num%10
    num = num//10
    reverse = reverse*10 + digit
print(reverse * sign)