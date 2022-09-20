"""
A sub policy is an incomplete policy that does not necessarily return a value
and can return a None value if it does not find anything interesting.

Sub policies all have the same typing: Callable[[Game, int, int], Optional[int]],
which allows them to be chained using utils.chain_sub_policies.
"""
from typing import Optional

from gonggi.simulation import Game, is_column_not_full


# noinspection PyUnusedLocal
def first_empty_column(game: Game, dice_value: int, player_index: int) -> Optional[int]:
    """
    Returns the first empty column if there is one.
    """
    return next(
        (
            col
            for col in range(game["board"]["size"])
            if len(game["board"]["grids"][player_index][col]) == 0
        ),
        None,
    )


# noinspection PyUnusedLocal
def first_non_full_column(game: Game, dice_value: int, player_index: int) -> int:
    """
    Returns the first non-full column. There will always be one as long as the game is running.
    """
    return next(
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(
            game["board"]["size"], game["board"]["grids"][player_index][col]
        )
    )


def stack(game: Game, dice_value: int, player_index: int) -> Optional[int]:
    """
    Returns the first column of the player's grid that already contains the dice_value.
    """
    return next(
        (
            col
            for col in range(game["board"]["size"])
            if dice_value in set(game["board"]["grids"][player_index][col])
            and is_column_not_full(
                game["board"]["size"], game["board"]["grids"][player_index][col]
            )
        ),
        None,
    )


def spread(game: Game, dice_value: int, player_index: int) -> Optional[int]:
    """
    Returns the first column of the player's grid that does not already contain the dice_value.
    """
    return next(
        (
            col
            for col in range(game["board"]["size"])
            if dice_value not in set(game["board"]["grids"][player_index][col])
            and is_column_not_full(
                game["board"]["size"], game["board"]["grids"][player_index][col]
            )
        ),
        None,
    )


def counter(game: Game, dice_value: int, player_index: int) -> Optional[int]:
    """
    Returns the first column the player can use to delete his opponent's dice if there is one.
    """
    return next(
        (
            col
            for col in range(game["board"]["size"])
            if dice_value in game["board"]["grids"][int(not player_index)][col]
            and is_column_not_full(
                game["board"]["size"], game["board"]["grids"][player_index][col]
            )
        ),
        None,
    )
