import math
#Prompt the user to enter the angle
x = int(input("Enter the angle  "))
#Convert the integer to degrees using radians function 
angle = math.radians(x)
# Use the sin cos and tan funtions
sin_val = math.sin(angle)
cos_val = math.cos(angle)
tan_val = math.tan(angle)
print("sin value is = ", sin_val)
print("cos value is = ", cos_val)
print("tan value is = ", tan_val)