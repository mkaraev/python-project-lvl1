import random
import math

from brain_games.games.base import Game, Round


class GCDGame(Game):
    def __init__(self):
        self.DESCRIPTION = "Find the greatest common divisor of given numbers."

    def generate_round(self) -> Round:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        question = f"{a} {b}"
        answer = str(math.gcd(a, b))
        return Round(question, answer)

    @property
    def description(self):
        return self.DESCRIPTION
