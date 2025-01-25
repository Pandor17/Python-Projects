import copy
import random
from collections import Counter


class Hat:
    def __init__(self, **kwargs: dict):
        if kwargs:
            self.contents = [color for color, valor in kwargs.items() for _ in range(valor)]

    def draw(self, num_balls_drawn: int) -> list:
        if num_balls_drawn > len(self.contents):
            balls_drawn = [self.contents.pop(0) for _ in range(len(self.contents))]
        else:
            balls_drawn = [self.contents.pop(random.randint(0, len(self.contents) - 1)) for bolas in
                           range(num_balls_drawn)]
        return balls_drawn


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    exito = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        drawn_counts = Counter(balls_drawn)
        if all(drawn_counts[ball] >= count for ball, count in expected_balls.items()):
            exito += 1
    probability = exito / num_experiments
    return probability


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)
