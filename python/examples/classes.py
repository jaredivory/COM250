class Point:
    def move(self):
        print("move")
    def draw(self):
        print(f"({self.x},{self.y})")

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
point1 = Point(10,20)
point1.draw()