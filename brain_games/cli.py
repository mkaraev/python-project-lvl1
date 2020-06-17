import prompt


def welcome():
    print("Welcome to the Brain Games!")


def print_message(message):
    print(message)


def ask_name():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def ask_question_and_read_answer(question):
    print_message(question)
    answer = prompt.string("Your answer: ")
    return answer.lower()

