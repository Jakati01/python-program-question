numbers = [1, 2, 2, 3, 4, 4, 5]
result =[]

for num in numbers:
    count =0

    for items in numbers:
        if  items ==num:
            count+=1

    if count==1:
        result.append(num)
print(result)