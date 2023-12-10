from typing import Callable

from gonggi.simulation.data_structures import Game
from gonggi.simulation.display import print_board


# noinspection PyUnusedLocal
def policy_template(game: Game, dice_value: int, player_index: int) -> int:
    """
    A policy will always take these two arguments.

    Args:
        game: The state of the game. You can retrieve the values on the board here.
        dice_value: The value of the die to place on the board.
        player_index: The index of the player who plays (0 for the first player, 1 for the second one).

    Returns:
        The index of the column to play on.
    """
    pass


def policy_cli(game: Game, dice_value: int, player_index: int) -> int:
    """
    Policy that consists in asking for user input.
    """
    print_board(game["board"])
    return int(
        input(
            f"{game['player_names'][player_index]} rolled a {dice_value}, in which column do you want to put it? "
        )
    )


def apply_to_player(
    policy: Callable[[Game, int, int], int], player_index: int
) -> Callable[[Game, int], int]:
    """
    Sets argument player_index for a policy.
    """
    return lambda game, dice: policy(game, dice, player_index)
