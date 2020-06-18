import prompt


def print_message(message):
    print(message)


def ask_name():
    name = prompt.string('May I have your name? ')
    return name


def read_answer():
    answer = prompt.string("Your answer: ")
    return answer.lower()
