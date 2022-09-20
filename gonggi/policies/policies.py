from gonggi.simulation import Game
from .sub_policies import (
    stack,
    first_empty_column,
    first_non_full_column,
    counter,
    greedy,
)
from .utils import chain_sub_policies


# noinspection PyUnusedLocal
def left_to_right(game: Game, dice_value: int, player_index: int) -> int:
    """
    Choosing the first available column.
    Can be used to benchmark a policy, any policy should be better than this one.
    """
    return first_non_full_column(game, dice_value, player_index)


def stack_first_then_fill(game: Game, dice_value: int, player_index: int) -> int:
    return chain_sub_policies(
        (game, dice_value, player_index),
        stack,
        first_empty_column,
        first_non_full_column,
    )


def fill_first_then_stack(game: Game, dice_value: int, player_index: int) -> int:
    return chain_sub_policies(
        (game, dice_value, player_index),
        first_empty_column,
        stack,
        first_non_full_column,
    )


def counter_then_stack(game: Game, dice_value: int, player_index: int) -> int:
    return chain_sub_policies(
        (game, dice_value, player_index),
        counter,
        stack,
        first_empty_column,
        first_non_full_column,
    )


def counter_then_fill(game: Game, dice_value: int, player_index: int) -> int:
    return chain_sub_policies(
        (game, dice_value, player_index),
        counter,
        first_empty_column,
        stack,
        first_non_full_column,
    )


def greedy_or_fill(game: Game, dice_value: int, player_index: int) -> int:
    return chain_sub_policies(
        (game, dice_value, player_index),
        greedy,
        first_empty_column,
        first_non_full_column,
    )
