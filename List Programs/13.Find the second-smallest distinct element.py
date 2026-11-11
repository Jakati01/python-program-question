numbers = [5, 2, 8, 1, 2, 4]

smallest = float("inf")
second_smallest = float("inf")

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num > smallest and num < second_smallest:
        second_smallest = num

if second_smallest == float("inf"):
    print(-1)
else:
    print(second_smallest)