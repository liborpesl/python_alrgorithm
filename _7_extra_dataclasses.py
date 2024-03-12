import dataclasses


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(4, 1)
point


@dataclasses.dataclass
class Point2:
    x: float
    y: float


point2 = Point2(4, 1)
point2.x
point2.y
print(point2)
