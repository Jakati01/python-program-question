'''''''''
arr = [1, 2, 3, -2, 5, -3]
target = 3
Question: Find the number of contiguous subarrays whose sum equals 3.
Expected answer:
5
'''''

def subarrays (arr,target):
    Prefix_Sum =0
    count =0
    frequency_prefixsum ={0:1}

    for num in arr:
        Prefix_Sum +=num

        needed = Prefix_Sum - target

        count += frequency_prefixsum.get(needed,0)

        frequency_prefixsum[Prefix_Sum] = frequency_prefixsum.get(Prefix_Sum,0)+1

    return count

arr = [1, 2, 3, -2, 5, -3]
target = 3
print(subarrays(arr,target))
