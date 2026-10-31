#while loop
num = int(input('ENTER THE NUMBER :'))
num = abs(num)
count = 0

if num ==0:
    count+=1
else:
    while num>0:
     num=num//10
     count+=1
print(count)

#built-fumction
num = int(input('ENTER THE NUMBER :'))
print(len(str(abs(num))))

