"""Write a Python program to calculate the area of regular polygon.
    Input number of sides: 4
    Input the length of a side: 25
    The area of the polygon is: 625"""

import math
sides = int(input())
length = float(input())
area = (sides*pow(length, 2))/4*math.tan(math.pi/sides)
area = round(area, 0)
print(area)