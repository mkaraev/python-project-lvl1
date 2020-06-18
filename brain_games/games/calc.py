import random

DESCRIPTION = "What is the result of the expression?"


def _generate_random_expression():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    op = random.choice(["+", "-", "*"])
    expr = f"{a} {op} {b}"
    return expr


def generate_question_answer_pair():
    expr = _generate_random_expression()
    answer = str(eval(expr))

    return expr, answer
