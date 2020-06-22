import random
import math

DESCRIPTION = "Answer \'yes\' if given number is prime. " \
              "Otherwise answer \'no\'."

MAX_NUM = 1000


def generate_question_answer():
    question = random.randint(0, MAX_NUM)
    answer = "yes" if _is_prime(question) else "no"
    return str(question), answer


def _is_prime(number):
    if number <= 1:
        return False

    d = math.ceil(math.sqrt(number)) + 1
    for i in range(2, d):
        if number % i == 0:
            return False
    return True
