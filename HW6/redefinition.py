class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __contains__(self, point) -> bool:
        return (point.x - self.x) ** 2 + (
                point.y - self.y) ** 2 <= self.radius ** 2


p1 = Point(1, 2)
c1 = Circle(1, 2, 10)
print(Point(-8, -6) in Circle(0, 0, 10))
print(Point(1, 2) in Circle(1, 2, 10))
print(p1 in c1)
print(Point(-8, -7) in Circle(0, 0, 10))
