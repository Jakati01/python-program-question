num = int(input("Enter a number: "))
num = abs(num)
odd =0
even =0
if num ==0:
    even=1

else:
    while num >0:
     digit = num%10
     if digit %2 ==0:
        even+=1
     else:
        odd+=1
     num = num//10
print(f'even number is {even}')
print(f'odd number is {odd}')
