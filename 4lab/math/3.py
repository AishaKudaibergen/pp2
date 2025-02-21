#Write a Python program to calculate the area of regular polygon
import math
n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
area = (n* s**2)/(4*math.tan(math.pi/n))
print("The area of the polygon is:", round(area))
