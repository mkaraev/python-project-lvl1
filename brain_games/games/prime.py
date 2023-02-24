import random
import math

from brain_games.games.base import Game, Round


def _is_prime(number):
    if number <= 1:
        return False

    sqrt_number = math.ceil(math.sqrt(number)) + 1
    for i in range(2, sqrt_number):
        if number % i == 0:
            return False
    return True


class PrimeGame(Game):
    def __init__(self):
        self.DESCRIPTION = "Answer \'yes\' if given number is prime. " \
                           "Otherwise answer \'no\'."

    def generate_round(self) -> Round:
        question = random.randint(0, 1000)
        answer = "yes" if _is_prime(question) else "no"
        return Round(str(question), answer)

    @property
    def description(self):
        return self.DESCRIPTION
