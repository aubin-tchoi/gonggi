import logging
from typing import Callable, Literal

from data_structures import Game, Board
from play import is_column_not_full, play_turn, update_scores
from utils import print_game_info, print_winner


def instantiate_new_game(
    board_size: int,
    n_sides: int,
    first_player_name: str,
    second_player_name: str,
) -> Game:
    """
    Creates a new game.

    Args:
        board_size: Size of the board (each player will play on a board_size x board_size grid).
        n_sides: Number of sides on the die.
        first_player_name: Name of the first player.
        second_player_name: Name of the second player.

    Returns:
        The newly created game.
    """
    logging.info(
        f"Launching a new game with a board of size {board_size} "
        f"using a {n_sides}-sided die "
        f"opposing {first_player_name} and {second_player_name}.\n"
    )
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


def is_board_not_full(game: Game) -> bool:
    """
    Finds out if there is room left on both players' sides of the grid.
    """
    return any(
        is_column_not_full(
            game["board"]["size"], game["board"]["first_player_grid"][col]
        )
        for col in range(game["board"]["size"])
    ) and any(
        is_column_not_full(
            game["board"]["size"], game["board"]["second_player_grid"][col]
        )
        for col in range(game["board"]["size"])
    )


def run_game(
    game: Game,
    first_player_policy: Callable[[Game, int], int],
    second_player_policy: Callable[[Game, int], int],
    logging_level: int,
) -> Literal["first", "second", "tie"]:
    """
    Plays the game until one side of the board is full.
    """
    while is_board_not_full(game):
        play_turn(game, first_player_policy, second_player_policy)
        update_scores(game)
        # check added to improve performances, see: https://docs.python.org/2/howto/logging.html#optimization
        if logging_level >= 20:
            print_game_info(game)

    return print_winner(game)
