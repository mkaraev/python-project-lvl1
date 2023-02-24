from brain_games import cli
from brain_games.games.base import Game, Round

ROUNDS_NUMBER = 3


def run(game: Game):
    print("Welcome to the Brain Games!")
    print(game.description)
    player_name = cli.ask("May I have your name? ")
    print(f"Hello, {player_name}!")

    for _ in range(ROUNDS_NUMBER):
        current_round: Round = game.generate_round()
        question = "Question: " + current_round.question
        print(question)
        user_answer = cli.ask("Your answer: ")

        if user_answer != current_round.answer:
            message = f"\'{user_answer}\' is wrong answer ;(. " \
                      f"Correct answer was \'{current_round.answer}\'.\n" \
                      f"Let\'s try again, {player_name}!"
            print(message)
            return
        else:
            print("Correct!")

    message = f"Congratulations, {player_name}!"
    print(message)
