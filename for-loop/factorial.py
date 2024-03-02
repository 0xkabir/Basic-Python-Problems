n = int(input("Enter the number you want to calculate factorial: "))
res = 1
for i in range(1, n+1):
    res *= i

print(f"factorial of {n}: {res}")