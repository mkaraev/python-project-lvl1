import random

DESCRIPTION = "Answer \'yes\' if given number is prime. " \
              "Otherwise answer \'no\'."

MAX_NUM = 1000
primes = []


def generate_question_answer_pair():
    random_number = random.randint(0, MAX_NUM)
    answer = "yes" if _is_prime(random_number) else "no"
    return f"{random_number}", answer


def _is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
