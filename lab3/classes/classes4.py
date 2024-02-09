class Point:
    def __init__(a, x, y):
        a.fc = x
        a.sc = y
    def show(a):
        print(a.fc, a.sc)
    def move(a, forx, fory):
        a.fc+=forx
        a.sc+=fory
    def dist(a, dx, dy):
        distance = ((a.fc-dx)**2+(a.sc-dy)**2)**(1/2)
        return distance
    
nykte = Point(4, 5)
nykte.show()
nykte.fc = 9
nykte.move(1, -80)
nykte.fc = nykte.sc = 0
print(nykte.dist(1, 8))
