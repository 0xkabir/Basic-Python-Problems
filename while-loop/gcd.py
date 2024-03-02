number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
max_range = min(number1, number2)
divider = 1
gcd = 1

while divider <= max_range:
    if (number1%divider == 0) & (number2%divider == 0):
        gcd = divider
    divider += 1

print(f"The GCD of {number1} and {number2} is {gcd}")