import random

from brain_games.games.base import Game, Round


def _is_even(number):
    return number % 2 == 0


class EvenGame(Game):
    def __init__(self):
        self.DESCRIPTION = "Answer 'yes' if number even otherwise answer 'no'."

    def generate_round(self) -> Round:
        question = random.randint(0, 1000)
        answer = "yes" if _is_even(question) else "no"
        return Round(str(question), answer)

    @property
    def description(self):
        return self.DESCRIPTION
