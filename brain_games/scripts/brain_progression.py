from brain_games import game_runner
from brain_games.games import progression


def main():
    game_runner.run(progression.ProgressionGame())


if __name__ == '__main__':
    main()
