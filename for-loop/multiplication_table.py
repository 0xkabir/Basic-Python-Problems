n = int(input('Enter the number you want to generate multiplication table: '))
print(f"Multiplication Table for {n}\n")
for i in range(1, 11):
    res = n * i
    print(f"{n} x {i} = {res}")