import random

DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10


def generate_question_answer_pair():
    global PROGRESSION_LENGTH

    first, difference = _generate_progression_params()
    progression = _generate_progression(first, difference, PROGRESSION_LENGTH)
    index = random.choice(range(len(progression)))
    missed_value = progression[index]

    progression = [str(number) for number in progression]
    progression[index] = ".."
    answer = str(missed_value)

    return " ".join(progression), answer


def _generate_progression(first, difference, length):
    values = []
    for i in range(length):
        values.append(first + difference * i)
    return values


def _generate_progression_params():
    first = random.randint(0, 10)
    difference = random.randint(0, 10)
    return first, difference
