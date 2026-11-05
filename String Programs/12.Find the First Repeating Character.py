text = input("Enter a string: ")

seen = set()
found=False
for char in text:
    if char in seen:
        print(char)
        found= True
        break
    seen.add(char)
if not found:
    print("No repeating character")



