number = int(input("Enter a number to reverse: "))
reversed_number = 0
print(f"reverse number of {number}", end=": ")

while number>0:
    remainder = number%10
    reversed_number = reversed_number*10 + remainder 
    number //=10

print(reversed_number)