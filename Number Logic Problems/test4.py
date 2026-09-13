''''''''''''''''''''''''''''''''''
arr = [3, 1, 4, 1, 5, 9, 3]
Question:Find the first element that appears more than once.
Expected:
1
'''''''''''''''''

def first_element(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return None
arr = [3, 1, 4, 1, 5, 9, 3]
print(first_element(arr))

# time compelixity o(n) and space complexity o(n)
''''''''''''''''
which data structure - I used set() -- hashset because - o(n) of seraching 


'''''