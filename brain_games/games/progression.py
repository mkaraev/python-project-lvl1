import random

DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10


def generate_question_answer():
    first = random.randint(0, 10)
    difference = random.randint(0, 10)
    progression = _generate_progression(first, difference, PROGRESSION_LENGTH)
    index = random.choice(range(PROGRESSION_LENGTH))
    missed_value = progression[index]

    progression = [str(number) for number in progression]
    progression[index] = ".."
    answer = str(missed_value)
    question = " ".join(progression)
    return question, answer


def _generate_progression(first, difference, length):
    progression = []
    for i in range(length):
        progression.append(first + difference * i)
    return progression
