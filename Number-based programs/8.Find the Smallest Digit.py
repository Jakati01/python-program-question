num = str(input("Enter a number: "))

num=int(abs(num))

smallest = num
if num ==0:
    smallest =0

else :
    while num >0:
     digit = num%10
   
     if smallest > digit:
         smallest = digit
     num=num//10
print("The smallest digit is:", smallest)