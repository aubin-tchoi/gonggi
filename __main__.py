import argparse
import logging
from random import seed

from gonggi import first_player_policy, second_player_policy, instantiate_new_game, run_game


def parse_args() -> argparse.Namespace:
    """
    Parses the CLI arguments passed to the main using argparse.

    Returns:
        The Namespace that stores the arguments passed.
    """
    parser = argparse.ArgumentParser(description="Main entry point for the simulator")

    parser.add_argument(
        "--p1",
        type=str,
        default="Julien",
        help="set the name of the first player",
    )
    parser.add_argument(
        "--p2",
        type=str,
        default="Aubin",
        help="set the name of the second player",
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=1,
        help="set the number of runs (if more than 1 run is performed, prints the distribution of wins)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=3,
        help="set the size of the board",
    )
    parser.add_argument(
        "--sides",
        type=int,
        default=6,
        help="set the number of sides on the dice",
    )
    parser.add_argument(
        "--deterministic_seed",
        action="store_true",
        help="use a deterministic seed to roll the dice (based on the players' names)",
    )
    parser.add_argument(
        "--no_verbose",
        action="store_true",
        help="do not log info on stdout",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="debug mode (more verbose)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.deterministic_seed:
        seed(args.p1 + args.p2)

    first_wins, second_wins, n_ties = 0, 0, 0
    logging_level = (
        logging.DEBUG
        if args.debug
        else logging.WARNING
        if args.no_verbose
        else logging.INFO
    )
    logging.basicConfig(format="%(message)s", level=logging_level)

    for _ in range(args.runs):
        my_game = instantiate_new_game(args.size, args.sides, args.p1, args.p2)

        # Set the policies of each player here.
        result = run_game(
            my_game,
            first_player_policy,
            second_player_policy,
            logging_level,
        )
        if result == "first":
            first_wins += 1
        elif result == "second":
            second_wins += 1
        elif result == "tie":
            n_ties += 1

    if args.runs > 1:
        print(
            f"\n{args.p1} won {first_wins} times, "
            f"{args.p2} {second_wins} times and there were {n_ties} ties."
        )
