def two_sum(arr, target):

    seen ={}

    for i, num in enumerate(arr):
        needed = target - num

        if needed in seen:
            return [seen[needed],i]
        seen[num] =i
    

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr,target))

        