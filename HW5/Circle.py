class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        x1 = point[0]
        y1 = point[1]
        if self.x <= x1 <= self.x + self.radius and \
                self.y <= y1 <= self.y + self.radius:
            return True
        elif self.x <= x1 <= self.x + self.radius and \
                self.y >= y1 >= self.y - self.radius:
            return True
        elif self.x >= x1 >= self.x - self.radius and \
                self.y >= y1 >= self.y - self.radius:
            return True
        elif self.x >= x1 >= self.x - self.radius and \
                self.y <= y1 <= self.y + self.radius:
            return True
        else:
            return False


class Point:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def point(self):
        return self.x1, self.y1


krug = Circle(0, 0, 10)
tochka = Point(1, 1)
print(krug.contains(tochka.point()))
