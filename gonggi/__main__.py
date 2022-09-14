import argparse

from policies import *
from simulator import instantiate_new_game, run_game


def parse_args() -> argparse.Namespace:
    """
    Parses the CLI arguments passed to the main using argparse.

    :return: The Namespace that stores the arguments passed.
    """
    parser = argparse.ArgumentParser(description="Main entry point for the simulator.")

    parser.add_argument(
        "--verbose", action="store_false", help="Sets the verbose to True."
    )
    parser.add_argument(
        "--p1",
        type=str,
        default="Julien",
        help="Sets the name of the first player.",
    )
    parser.add_argument(
        "--p2",
        type=str,
        default="Aubin",
        help="Sets the name of the second player.",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=3,
        help="Sets the size of the board.",
    )
    parser.add_argument(
        "--sides",
        type=int,
        default=6,
        help="Sets the number of sides on the dice.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    my_game = instantiate_new_game(args.size, args.sides, args.p1, args.p2)
    run_game(my_game, first_player_naive_policy, second_player_naive_policy)
