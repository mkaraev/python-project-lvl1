from brain_games import cli

ROUNDS_NUMBER = 3


def run(game):
    print("Welcome to the Brain Games!")
    print(game.DESCRIPTION)
    player_name = cli.ask("May I have your name? ")
    print(f"Hello, {player_name}!")

    for _ in range(ROUNDS_NUMBER):
        question, answer = game.generate_question_answer()
        question = "Question: " + question
        print(question)
        user_answer = cli.ask("Your answer: ")

        if user_answer != answer:
            message = f"\'{user_answer}\' is wrong answer ;(. " \
                      f"Correct answer was \'{answer}\'.\n" \
                      f"Let\'s try again, {player_name}!"
            print(message)
            return
        else:
            print("Correct!")

    message = f"Congratulations, {player_name}!"
    print(message)
