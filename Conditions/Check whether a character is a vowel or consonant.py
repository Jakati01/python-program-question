'''
Check whether a character is a vowel or consonant
'''
character = input('Enter the character : ')

if len(character) !=1:
    print(f'PLEASE ENTER CORRECT STRING ')

elif character =='a' or character =='e' or character =='i' or character == 'o' or  character =='u':
    print(f'{character} is vowel')

elif character =='A' or character =='E' or character =='I' or character == 'O' or  character =='U':
    print(f'{character} is vowel')

else:
    print(f'{character} it is invaild character')