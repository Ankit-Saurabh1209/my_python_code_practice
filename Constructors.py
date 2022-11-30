class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Move(self):
        print("move")

    def Draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)
