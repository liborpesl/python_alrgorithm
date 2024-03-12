import random

random.random()


def estimate_pi(n: int):
    points = []

    for i in range(n):
        x = random.random()
        y = random.random()

        points.append((x, y))

    points_in_circle = []

    for point in points:
        dist = (point[0] ** 2 + point[1] ** 2) ** (1 / 2)
        if dist <= 1:
            points_in_circle.append(point)

    return (4 * len(points_in_circle) / len(points))


estimate_pi(100)

for n in [20, 100, 250, 500, 1000, 5000, 20000, 100_000, 1_000_000]:
    print(f"Estimated pi from {n=}: ", estimate_pi(n))


def get_random_point():
    x = random.random()
    y = random.random()
    return x, y


def calculate_distance(point: tuple[float, float]):
    return (point[0] ** 2 + point[1] ** 2) ** (1 / 2)


def calculate_distance_from_origin(point: tuple[float, float]):
    return (point[0] ** 2 + point[1] ** 2) ** (1 / 2)


def estimate_pi_refactored(n: int):
    number_of_points_in_circle = 0

    for i in range(n):
        point = get_random_point()

        if calculate_distance_from_origin(point) <= 1:
            number_of_points_in_circle += 1

    return 4 * number_of_points_in_circle / n


for n in [20, 100, 250, 500, 1000, 5000, 20000, 100_000, 1_000_000, 100_000_000]:
    print(f"Estimated pi from {n=}: ", estimate_pi_refactored(n))


# 100 000 000
#
# 3.1415 4292
# 3.1415 92653589793


class PiEstimator:

    def __init__(self):
        self.number_of_points_in_circle = 0
        self.number_of_points_total = 0

    def estimate_pi_refactored(self, n: int):

        for i in range(n):
            self.number_of_points_total += 1
            point = get_random_point()

            if calculate_distance_from_origin(point) <= 1:
                self.number_of_points_in_circle += 1

        return 4 * self.number_of_points_in_circle / self.number_of_points_total


# pi_estimator = PiEstimator()

for n in [20, 100, 250, 500, 1000, 5000, 20000, 100_000, 1_000_000, 100_000_000]:
    pi_estimation = pi_estimator.estimate_pi_refactored(n)
    print(f"Estimated pi from {pi_estimator.number_of_points_total=}: ", pi_estimation)


3.1415 5335767833
3.1415 92653589793
