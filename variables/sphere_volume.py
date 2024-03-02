from math import pi, pow
radius = float(input("Enter radius of the sphere: "))
volume = round((4/3)*pi*pow(radius, 3), 2)

print(f"volume of a sphere with radius {radius} units: {volume} cubic units")