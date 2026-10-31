num = int(input("Enter a number: "))
total = 0

if num > 1:
    for i in range(1, num):
        if num % i == 0:
            total += i

if total == num and num > 0:
    print("It is a perfect number")
else:
    print("It is not a perfect number")