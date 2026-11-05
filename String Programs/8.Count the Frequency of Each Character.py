text = input("Enter a string: ")

seen= {}

for char in text:
    if char in seen:
        seen[char]+=1
    else:
        seen[char]=1
print(seen)