import logging
from typing import Literal

from gonggi.simulation import (
    Board,
    Game,
    Policy,
    is_column_not_full,
    play_turn,
    print_game_info,
    print_winner,
    update_scores,
)


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
            grids=([[] for _ in range(board_size)], [[] for _ in range(board_size)]),
        ),
        player_scores=(0, 0),
        player_names=(first_player_name, second_player_name),
    )


def is_board_not_full(game: Game) -> bool:
    """
    Finds out if there is room left on both players' sides of the grid.
    """
    return all(
        any(
            is_column_not_full(game["board"]["size"], grid[col])
            for col in range(game["board"]["size"])
        )
        for grid in game["board"]["grids"]
    )


def run_game(
    game: Game, first_player_policy: Policy, second_player_policy: Policy
) -> Literal["first", "second", "tie"]:
    """
    Plays the game until one side of the board is full.
    """
    while is_board_not_full(game):
        play_turn(game, first_player_policy)
        play_turn(game, second_player_policy, 1)
        update_scores(game)
        print_game_info(game)

    return print_winner(game)
