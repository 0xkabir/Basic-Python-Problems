n = int(input("Enter the number you want to calculate sum: "))
i = 2
result = 0
while i <= n:
    result += i
    i += 2
    
print(f"Sum of all even numbers from 0 to {n}: {result}")