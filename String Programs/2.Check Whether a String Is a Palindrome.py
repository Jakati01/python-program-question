#Method 1: Two pointers — recommended 
#Time: O(n) · Extra space: O(1)
'''''''''
text = input("Enter a string: ")
left =0
right = len(text)-1
is_palindrome = False

while left <right:
    if text[left] == text[right]:
        is_palindrome= True
        break
    left+=1
    right-=1
if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#Time: O(n) · Extra space: O(1)

------------------     -------------------   -----------------------
#Method 2: Loop and reverse
#Time: O(n²) with repeated string concatenation · Extra space: O(n)

text = input("Enter a string: ")
orginal_text = text
reversed_text=''

for char in text:
    reversed_text=char+reversed_text
if orginal_text == reversed_text:
    print('It is Palindrome')
else:
    print('It is not Palindrome')

-------------------- -------------------------------------
#Method 3: Python slicing
#Time: O(n) · Extra space: O(n)

text = input("Enter a string: ")
reversed_text=text[::-1]
if text == reversed_text:
     print('It is Palindrome')
else:
        print('It is not Palindrome')

'''''''''''''''''
