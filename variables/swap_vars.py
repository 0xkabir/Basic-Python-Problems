var1 = input("Enter first variable: ")
var2 = input("Enter second variable: ")

print(f"variables before swap: {var1}, {var2}")

temp_var = var1
var1 = var2
var2 = temp_var

print(f"variables after swap: {var1}, {var2}")