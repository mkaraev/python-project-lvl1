from brain_games import cli


def run(game):
    cli.welcome()
    cli.print_message(game.DESCRIPTION)
    player_name = cli.ask_name()
    win = True
    for _ in range(3):
        question, answer = game.generate_question_answer_pair()
        user_answer = cli.ask_question_and_read_answer(question)
        if user_answer != answer:
            win = False
            message = f"\'{user_answer}\' is wrong answer ;(. " \
                      f"Correct answer was \'{answer}\'.\n" \
                      f"Let\'s try again, {player_name}!"
            cli.print_message(message)
            break
        else:
            cli.print_message("Correct!")
    if win:
        message = f"Congratulations, {player_name}!"
        cli.print_message(message)
