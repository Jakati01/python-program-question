#Approach 1 — Python built-in function
numbers=[10, 25, 7, 40, 15]
print(min(numbers))

#Approach 2 — Manual loop (logic-based)
numbers=[10, 25, 7, 40, 15]
smallest=numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest)