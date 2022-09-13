import argparse


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
        help="Changes the name of the first player.",
    )
    parser.add_argument(
        "--p2",
        type=str,
        default="Aubin",
        help="Changes the name of the second player.",
    )

    return parser.parse_args()


def run_game(first_player_name: str, second_player_name: str) -> None:
    pass


if __name__ == "__main__":
    args = parse_args()
    run_game(args.p1, args.p2)
