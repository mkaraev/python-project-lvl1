from brain_games import game_runner
from brain_games.games import even


def main():
    game_runner.run(even.EvenGame())


if __name__ == '__main__':
    main()
