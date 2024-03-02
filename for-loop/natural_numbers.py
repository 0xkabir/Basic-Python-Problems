last_number = int(input("Enter the value for n: "))
print('n natural numbers: ')
for i in range(1, last_number+1):
    if i==last_number:
        print(i)
    else:
        print(i, end=', ')