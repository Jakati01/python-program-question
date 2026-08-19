''''''''''''''''
Check whether a character is uppercase or lowercase.

'''''''''''
character = input("Enter a character: ")

if character.isupper():
    print("Uppercase")
elif character.islower():
    print("Lowercase")
else:
    print("Not an alphabet character or Please type one word") 