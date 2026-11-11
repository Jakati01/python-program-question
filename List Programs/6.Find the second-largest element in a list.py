numbers=[10, 25, 7, 40, 15]
largest=None
second_largest=None

for num in numbers:
    if largest is None or num>largest:
        second_largest = largest
        largest = num
    elif num!=largest and(num>second_largest or second_largest is None ):
        second_largest = num
print(second_largest)