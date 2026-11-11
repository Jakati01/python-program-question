#Approach 1 — Python built-in method
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

#Approach 2 — Manual loop (logic-based)
numbers = [10, 20, 30, 40, 50]
left =0
right =len(numbers)-1
while left<right:
    numbers[left],numbers[right]=numbers[right],numbers[left]
    left+=1
    right-=1
print(numbers)
