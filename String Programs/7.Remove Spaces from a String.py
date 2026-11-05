'''''''''''''''''''''
text = input("Enter a string: ")

no_spaces =''
for char in text:
    if char!=' ':
        no_spaces+=char
print(no_spaces)
'''''
text = input("Enter a string: ")
no_spaces = text.replace(" ","")
print(no_spaces)