num = int(input("Enter a number: "))
target = int(input("Enter the digit to count: "))

num =abs(num)
count =0
while num >0:
    digit = num %10
    if digit == target :
        count +=1
    num = num //10
print(count)