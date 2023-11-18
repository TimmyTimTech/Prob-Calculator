import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        return random.sample(self.contents, num)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        new_hat = Hat(**{color: count for color, count in hat.contents.items()})
        drawn_balls = new_hat.draw(num_balls_drawn)
        drawn_balls_dict = {color: drawn_balls.count(color) for color in expected_balls}
        if all(drawn_balls_dict[color] >= expected_balls[color] for color in expected_balls):
            count += 1
    return count / num_experiments
