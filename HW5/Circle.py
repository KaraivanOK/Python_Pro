class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point) -> bool:
        return (point.x - self.x) ** 2 + (
                point.y - self.y) ** 2 <= self.radius ** 2


my_circle = Circle(0, 0, 10)
my_point = Point(8, 8)
print(my_circle.contains(my_point))
