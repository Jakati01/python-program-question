text = input("Enter a string: ")

letters = 0
digits = 0
special = 0

for char in text:
    if char.isalpha():
        letters +=1
    elif char.isdigit():
        digits +=1
    else:
        special +=1
print(f'letters : {letters}')
print(f'digits : {digits}')
print(f'Special : {special}')