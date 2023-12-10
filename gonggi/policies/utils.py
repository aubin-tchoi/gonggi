from typing import Callable, Optional

from gonggi.simulation import Board, Game, is_column_not_full


def chain_sub_policies(
    args: tuple[Game, int, int],
    *sub_policies: Callable[[Game, int, int], Optional[int]],
) -> int:
    """
    Chains multiple sub policies using the following pattern: a sub policy that return a None value should be ignored.
    """
    return next(
        move for sub_policy in sub_policies if (move := sub_policy(*args)) is not None
    )


def chain_set_policies(
    args: tuple[Game, int, int],
    *set_policies: Callable[[Game, int, int], set[int]],
) -> int:
    """
    Chains multiple policies that each return a set of acceptable values.
    """
    return set.intersection(
        *list(super_policy(*args) for super_policy in set_policies)
    ).pop()


def chain_score_policies(
    args: tuple[Game, int, int],
    *score_policies: Callable[[Game, int, int], list[int]],
) -> int:
    """
    Chains multiple policies that each return a list of the scores of each column.
    """
    board_size = args[0]["board"]["size"]
    total_score = [sum(s) for s in zip(*map(lambda p: p(*args), score_policies))]
    return max(
        filter(
            lambda col: is_column_not_full(
                board_size, args[0]["board"]["grids"][args[2]][col]
            ),
            range(board_size),
        ),
        key=lambda col: total_score[col],
    )


def board_fullness(board: Board) -> tuple[int, int]:
    """
    Finds the proportion of each side of the board that contains dices.
    """
    return (
        sum(len(col) for col in board["grids"][0]) / board["size"] ** 2,
        sum(len(col) for col in board["grids"][1]) / board["size"] ** 2,
    )


def filter_admissible_values(
    filter_function: Callable[[int], bool], game: Game, player_index: int
) -> set[int]:
    return set(
        filter(
            lambda col: filter_function(col)
            and is_column_not_full(
                game["board"]["size"], game["board"]["grids"][player_index][col]
            ),
            range(game["board"]["size"]),
        )
    )


def sub_policy_to_score_policy(
    sub_policy: Callable[[Game, int, int], Optional[int]]
) -> Callable[[Game, int, int], list[int]]:
    """
    Converts a sub policy into a score policy (with a score of 1 on the chosen column and zero elsewhere).
    """
    return lambda game, dice_value, player_index: [
        1 if i == sub_policy(game, dice_value, player_index) else 0
        for i in range(game["board"]["size"])
    ]
