#Approach 1 — Python built-in tool


#Approach 2 — Manual loop (hash map / dictionary)
numbers = [1, 2, 2, 3, 1, 2]
seen={}
for num in numbers:
    if num in seen:
        seen[num] +=1
    else:
        seen[num] =1
print(seen)
