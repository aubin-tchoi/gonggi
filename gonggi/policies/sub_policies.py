"""
A sub policy is an incomplete policy that does not necessarily return a value
and can return a None value if it does not find anything interesting.

Sub policies all have the same typing: Callable[[Game, int, int], Optional[int]],
which allows them to be chained using utils.chain_sub_policies.
"""
from copy import deepcopy
from typing import Optional

from gonggi.simulation import compute_scores, Game, delete_dices, is_column_not_full


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


def greedy(game: Game, dice_value: int, player_index: int) -> Optional[int]:
    best_score, best_move = (
        game["player_scores"][player_index]
        - game["player_scores"][int(not player_index)],
        None,
    )
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
            # finding out about multiple maxima
            elif score == best_score:
                best_move = None

    return best_move
