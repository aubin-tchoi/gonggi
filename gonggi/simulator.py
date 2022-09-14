import argparse
from typing import Callable

from data_structures import Game, Board
from play import is_column_not_full, play_turn, update_scores
from policies import policy_cli, naive_policy
from utils import print_game_info


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
    parser.add_argument(
        "--size",
        type=int,
        default=3,
        help="Changes the size of the board.",
    )
    parser.add_argument(
        "--sides",
        type=int,
        default=6,
        help="Changes the number of sides on the dice.",
    )

    return parser.parse_args()


def instantiate_new_game(
    board_size: int,
    n_sides: int,
    first_player_name: str,
    second_player_name: str,
) -> Game:
    return Game(
        n_sides=n_sides,
        board=Board(
            size=board_size,
            first_player_grid=[[] for _ in range(board_size)],
            second_player_grid=[[] for _ in range(board_size)],
        ),
        first_player_score=0,
        second_player_score=0,
        first_player_name=first_player_name,
        second_player_name=second_player_name,
    )


def run_game(
    game: Game,
    first_player_policy: Callable[[Game, int], int],
    second_player_policy: Callable[[Game, int], int],
) -> None:
    while any(
        is_column_not_full(
            game["board"]["size"], game["board"]["first_player_grid"], col
        )
        for col in range(game["board"]["size"])
    ) and any(
        is_column_not_full(
            game["board"]["size"], game["board"]["second_player_grid"], col
        )
        for col in range(game["board"]["size"])
    ):
        play_turn(game, first_player_policy, second_player_policy)
        update_scores(game)
        print_game_info(game)


if __name__ == "__main__":
    args = parse_args()
    my_game = instantiate_new_game(args.size, args.sides, args.p1, args.p2)
    run_game(my_game, naive_policy, policy_cli)
