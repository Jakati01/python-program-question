#Approach 1 — Built-in
numbers = [10, 25, 7, 40, 15]
print(max(numbers))


#Approach 2 — Manual loop
numbers = [10, 25, 7, 40, 15]
largest=numbers[0]
for num in numbers:
    if num > largest:
     largest = num
print(largest)
