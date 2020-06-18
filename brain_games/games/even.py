import random

DESCRIPTION = "Answer 'yes' if number even otherwise answer 'no'."


def _is_even(number):
    return number % 2 == 0


def generate_question_answer_pair():
    number = random.randint(0, 1000)
    answer = "yes" if _is_even(number) else "no"

    return str(number), answer
