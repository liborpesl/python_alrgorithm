import random
from memory_profiler import profile


class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def get_random(cls):
        return cls(random.random(), random.random())


class PointOptimized:

    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def get_random(cls):
        return cls(random.random(), random.random())


my_point = Point(0.5, 0.5)
my_random_point = Point.get_random()

my_optimized_point = PointOptimized(0.5, 0.5)
my_optimized_point.y

# my_optimized_point.c = 123
my_optimized_point.x = 234
my_optimized_point.x
my_point.c = 123

def get_random_points():
    points = [Point.get_random() for i in range(1_000_000)]
    return points

def get_random_optimized_points():
    points = [PointOptimized.get_random() for i in range(1_000_000)]
    return points

@profile
def main():
    points = get_random_points()

    points_optimized = get_random_optimized_points()


if __name__ == '__main__':
    main()
