num = int(input("Enter the number: "))

original = num
temp = abs(num)
power = len(str(temp))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if num >= 0 and total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
