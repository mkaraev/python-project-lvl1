import random
from brain_games.games.base import Game, Round


def _generate_random_expression():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    op = random.choice(["+", "-", "*"])
    expr = f"{a} {op} {b}"
    return expr


def _calc(expression):
    a, op, b = expression.split()
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b


class CalcGame(Game):
    def __init__(self):
        self.DESCRIPTION = "What is the result of the expression?"

    def generate_round(self) -> Round:
        question = _generate_random_expression()
        answer = str(_calc(question))
        return Round(question, answer)

    @property
    def description(self) -> str:
        return self.DESCRIPTION
