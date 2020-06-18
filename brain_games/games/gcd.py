import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_question_answer_pair():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    answer = str(math.gcd(a, b))

    return f"{a} {b}", answer
