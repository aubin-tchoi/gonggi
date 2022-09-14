import argparse
from random import seed

from policies import *
from simulator import instantiate_new_game, run_game


def parse_args() -> argparse.Namespace:
    """
    Parses the CLI arguments passed to the main using argparse.

    Returns:
        The Namespace that stores the arguments passed.
    """
    parser = argparse.ArgumentParser(description="Main entry point for the simulator.")

    parser.add_argument(
        "--p1",
        type=str,
        default="Julien",
        help="set the name of the first player.",
    )
    parser.add_argument(
        "--p2",
        type=str,
        default="Aubin",
        help="set the name of the second player.",
    )
    parser.add_argument(
        "--n_runs",
        type=int,
        default=1,
        help="set the number of runs. If more than 1 run is performed, prints the distribution of wins.",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=3,
        help="set the size of the board.",
    )
    parser.add_argument(
        "--sides",
        type=int,
        default=6,
        help="set the number of sides on the dice.",
    )
    parser.add_argument(
        "--deterministic_seed",
        action="store_true",
        help="use a deterministic seed to roll the dice (based on the players' names).",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.deterministic_seed:
        seed(args.p1 + args.p2)

    first_wins, second_wins, n_ties = 0, 0, 0

    for _ in range(args.n_runs):
        my_game = instantiate_new_game(args.size, args.sides, args.p1, args.p2)

        # Set the policies of each player here.
        result = run_game(
            my_game, first_player_naive_policy, second_player_naive_policy
        )
        if result == "first":
            first_wins += 1
        elif result == "second":
            second_wins += 1
        elif result == "tie":
            n_ties += 1
    if args.n_runs > 1:
        print(
            f"\n{args.p1} won {first_wins} times, "
            f"{args.p2} {second_wins} times and there were {n_ties} ties."
        )
