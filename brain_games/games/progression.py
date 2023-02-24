import random

from brain_games.games.base import Game, Round

PROGRESSION_LENGTH = 10


def _generate_progression(first, difference, length):
    progression = []
    for i in range(length):
        progression.append(first + difference * i)
    return progression


class ProgressionGame(Game):
    def __init__(self):
        self.DESCRIPTION = "What number is missing in the progression?"

    def generate_round(self) -> Round:
        first = random.randint(0, 10)
        difference = random.randint(0, 10)
        progression = _generate_progression(first, difference, PROGRESSION_LENGTH)
        index = random.choice(range(PROGRESSION_LENGTH))
        missed_value = progression[index]

        progression = [str(number) for number in progression]
        progression[index] = ".."
        answer = str(missed_value)
        question = " ".join(progression)
        return Round(question, answer)

    @property
    def description(self):
        return self.DESCRIPTION
