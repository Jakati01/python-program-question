'''''''''''''''''''''''''''''''''''''''''''''''
arr = [4, 1, 2, 1, 4, 5, 2]
Find the first element that appears only once.
Expected:
5
'''''''''''''''''''''''''''''''''''''''''''''''''''

def first_element(arr):
    counts ={}

    for num in arr:
        counts[num] = counts.get(num,0)+1

    for num in arr:
        if counts[num] ==1:
            return num

    return None
        

arr = [4, 1, 2, 1, 4, 5, 2]
print(first_element(arr))   