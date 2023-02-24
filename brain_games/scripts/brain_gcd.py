from brain_games import game_runner
from brain_games.games import gcd


def main():
    game_runner.run(gcd.GCDGame())


if __name__ == '__main__':
    main()
