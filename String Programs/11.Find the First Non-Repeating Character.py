text = input("Enter a string: ")

seen = {}

for char in text:
    if char not in seen:
        seen[char] = 1
    else:
        seen[char] += 1

found = False

for key, value in seen.items():
    if value == 1:
        print(key)
        found = True
        break

if not found:
    print("No non-repeating character")