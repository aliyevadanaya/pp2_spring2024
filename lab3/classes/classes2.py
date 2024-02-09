class Shape:
    def __init__(s, c=0):
        s.length = c
        s.area = s.length ** 2
    def Area(s):
        print(s.area)

class Square(Shape):
    def _init__(s, a):
        Shape.__init__(a)
        s.length = a
        
