num = int(input("ENTER THE NUM: "))

a = 0
b = 1
total = 0

for _ in range(num):
    total += a
    a, b = b, a + b

print("Fibonacci sum =", total)
