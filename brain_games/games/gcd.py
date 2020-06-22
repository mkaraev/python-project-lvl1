import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_question_answer():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    question = f"{a} {b}"
    answer = str(math.gcd(a, b))
    return question, answer
