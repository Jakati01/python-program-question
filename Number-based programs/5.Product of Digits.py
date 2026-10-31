num = int(input("Enter a number: "))
num = abs(num)
product = 1

if num == 0:
    product = 0
else:
    while num > 0:
        digit = num % 10
        product *= digit
        num = num // 10
print(product)
