word = input('ENTER THE STRING : ')

word=word.lower()
vowels ='aeiou'
vowels_count =0
consonants_count =0

for char in word:
    if char.isalpha():
        if char in vowels:
         vowels_count +=1
        else:
            consonants_count +=1
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")