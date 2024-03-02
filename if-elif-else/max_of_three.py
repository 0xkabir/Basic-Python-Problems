num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print(f"{num1} is the largest number" if num1>num2 & num1>num3 else f"{num2} is the largest number" if num2>num1 & num2>num3 else f"{num3} is the largest number")