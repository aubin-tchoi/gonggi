import argparse
import logging
from math import sqrt
from random import seed

from gonggi import (
    instantiate_new_game,
    instantiate_new_single_player_game,
    run_game,
    run_single_player_game,
)
from gonggi.policies import (
    first_player_policy,
    second_player_policy,
    single_player_policy,
)


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
        help="set the name of the first player",
    )
    parser.add_argument(
        "--p2",
        type=str,
        default="Aubin",
        help="set the name of the second player",
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
    game_settings = parser.add_argument_group("Game settings")
    game_settings.add_argument(
        "--single_player",
        action="store_true",
        help="single player mode",
    )
    game_settings.add_argument(
        "--runs",
        type=int,
        default=1,
        help="set the number of runs (if more than 1 run is performed, prints the distribution of wins)",
    )
    game_settings.add_argument(
        "--size",
        type=int,
        default=3,
        help="set the size of the board",
    )
    game_settings.add_argument(
        "--sides",
        type=int,
        default=6,
        help="set the number of sides on the dice",
    )
    game_settings.add_argument(
        "--deterministic_seed",
        action="store_true",
        help="use a deterministic seed to roll the dice (based on the players' names)",
    )

    return parser.parse_args()


def main(args: argparse.Namespace = parse_args()) -> None:
    if args.deterministic_seed:
        seed(args.p1 + args.p2)

    logging_level = (
        logging.DEBUG
        if args.debug
        else logging.WARNING
        if args.no_verbose
        else logging.INFO
    )
    logging.basicConfig(format="%(message)s", level=logging_level)

    if args.single_player:
        mean, stddev = 0.0, 0.0
        for run in range(args.runs):
            my_game = instantiate_new_single_player_game(args.size, args.sides)
            final_score = run_single_player_game(my_game, single_player_policy)
            stddev = sqrt(
                (run - 1) / (run or 1) * stddev**2
                + (final_score - mean) ** 2 / (run + 1)
            )
            mean = (mean * run + final_score) / (run + 1)
        print(f"Mean score over {args.runs} runs: {mean:.2f}, stddev: {stddev:.2f}")
    else:
        first_wins, second_wins, n_ties = 0, 0, 0
        for _ in range(args.runs):
            my_game = instantiate_new_game(args.size, args.sides, args.p1, args.p2)

            result = run_game(my_game, first_player_policy, second_player_policy)
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


if __name__ == "__main__":
    main()
