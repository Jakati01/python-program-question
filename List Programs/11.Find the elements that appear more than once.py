numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = []

for num in numbers:
    count = 0

    for item in numbers:
        if item == num:
            count += 1

    if count > 1 and num not in result:
        result.append(num)
print(result)