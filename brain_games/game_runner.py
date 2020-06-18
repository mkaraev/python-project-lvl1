from brain_games import cli


def run(game):
    cli.print_message("Welcome to the Brain Games!")
    cli.print_message(game.DESCRIPTION)
    player_name = cli.ask_name()
    cli.print_message(f"Hello, {player_name}!")

    for _ in range(3):
        question, answer = game.generate_question_answer_pair()
        question = "Question: " + question
        cli.print_message(question)
        user_answer = cli.read_answer()

        if user_answer != answer:
            message = f"\'{user_answer}\' is wrong answer ;(. " \
                      f"Correct answer was \'{answer}\'.\n" \
                      f"Let\'s try again, {player_name}!"
            cli.print_message(message)
            return
        else:
            cli.print_message("Correct!")

    message = f"Congratulations, {player_name}!"
    cli.print_message(message)
