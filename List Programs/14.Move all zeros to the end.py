numbers = [0, 1, 0, 3, 12]

read=0
for write in range(len(numbers)):
    if numbers [write]!=0:
        numbers[read] = numbers[write]
        read +=1
while read < (len(numbers)):
     numbers[read]=0
     read +=1
print(numbers)
        