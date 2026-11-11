numbers = [1, 2, 2, 3, 4, 4, 5]
seen = set(numbers) 
for num in numbers:
    if num in seen:
        print(seen)


