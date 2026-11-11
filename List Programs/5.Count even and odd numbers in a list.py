numbers = [10, 15, 20, 25, 30]
even =0
odd =0
for num in numbers:
    if num%2==0:
        even +=1
    else:
        odd +=1
print(f'even:{even}')
print(f'odd:{odd}')