num = int(input("Enter a number: "))

if num < 0:
    print("Square root of a negative number is not supported")
else:
    for i in range(num + 1):
        if i * i == num:
            print("Square root =", i)
            break
    else:
        print("Not a perfect square")
