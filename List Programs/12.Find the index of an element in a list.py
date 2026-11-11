numbers = [10, 20, 30, 40,50]
target = 50
result = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        result = i
        break

print(result)
