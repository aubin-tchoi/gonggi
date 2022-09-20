from copy import deepcopy

from gonggi.simulation import compute_scores, Game, delete_dices, is_column_not_full
from .sub_policies import (
    stack,
    first_empty_column,
    first_non_full_column,
    counter,
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


def greedy(game: Game, dice_value: int, player_index: int) -> int:
    best_score, best_move = (
        game["player_scores"][player_index]
        - game["player_scores"][int(not player_index)],
        None,
    )
    # TODO: combine with another policy to choose between multiple maxima
    for move in range(game["board"]["size"]):
        if is_column_not_full(
            game["board"]["size"], game["board"]["grids"][player_index][move]
        ):
            # computing the hypothetical score if the player were to do this move
            board_copy = deepcopy(game["board"])
            board_copy["grids"][player_index][move].append(dice_value)
            delete_dices(dice_value, move, board_copy["grids"][int(not player_index)])
            updated_scores = compute_scores(board_copy)
            if (
                score := updated_scores[player_index]
                - updated_scores[int(not player_index)]
            ) > best_score:
                best_score, best_move = score, move

    return (
        best_move
        if best_move is not None
        else first_non_full_column(game, dice_value, player_index)
    )
