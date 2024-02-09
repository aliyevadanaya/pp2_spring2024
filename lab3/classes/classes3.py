# from classes2 import *
import classes2
class Rectangle(classes2.Shape):
    def __init__(a, length, width):
        super().__init__()
        a.l = length
        a.w = width
    def compute_area(a):
        a.area = a.l*a.w
x = Rectangle(4, 5)
x.compute_area()
x.Area()