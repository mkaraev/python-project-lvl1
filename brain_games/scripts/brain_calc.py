from brain_games import game_runner
from brain_games.games import calc


def main():
    game_runner.run(calc.CalcGame())


if __name__ == '__main__':
    main()
