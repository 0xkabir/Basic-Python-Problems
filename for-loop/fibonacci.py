n = int(input("Enter the range you want to generate the series: "))
a = 0
b = 1
print(f"fibonacci series of length {n}: ")
if n == 1:
    print(a)
elif n == 2:
    print(f"{a}, {b}")
else:
    print(f"{a}, {b}", end=", ")
    for i in range(3, n+1):
        c = a+b
        if i == n:
            print(c)
        else:
            print(c, end=", ")
        a = b
        b = c
        