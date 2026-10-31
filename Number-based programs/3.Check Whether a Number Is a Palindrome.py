num = int(input("ENTER THE NUMBER: "))

if num < 0:
    print(f"{num}, not palindrome")
else:
    original = num
    reverse_num = 0

    while num > 0:
        last_digit = num % 10
        num = num // 10
        reverse_num = reverse_num * 10 + last_digit

    if original == reverse_num:
        print(f"{original}, it is palindrome")
    else:
        print(f"{original}, not palindrome")
