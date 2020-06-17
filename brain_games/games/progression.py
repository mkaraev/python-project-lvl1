import random
import math

DESCRIPTION = "What number is missing in the progression?"


def _generate_progression():
    a = random.randint(1, 10)
    d = random.randint(1, 10)
    values = []
    for i in range(10):
        values.append(a + d * i)
    return values


def generate_question_answer_pair():
    progression = _generate_progression()
    index = random.choice(range(10))
    missed_value = progression[index]
    progression = [str(number) for number in progression]
    progression[index] = ".."
    answer = str(missed_value)

    return f"Question: " + " ".join(progression), answer
