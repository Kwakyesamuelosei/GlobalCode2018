import math
PI = math.pi
print(PI)
radius = float(input('Please Enter the Radius of a Sphere: \n'))
sa =  4 * PI * radius * radius
Volume = (4 / 3) * PI * radius * radius * radius
 
print("\n The Surface area of a Sphere = %.2f" %sa)
print("\n The Volume of a Sphere = %.2f" %Volume)
