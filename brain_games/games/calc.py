import random

DESCRIPTION = "What is the result of the expression?"


def generate_question_answer():
    question = _generate_random_expression()
    answer = str(_calc(question))
    return question, answer


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
