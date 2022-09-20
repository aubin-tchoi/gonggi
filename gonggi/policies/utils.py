from gonggi.simulation.data_structures import Game, Board
from typing import Tuple, Callable, Optional


def chain_sub_policies(
    args: Tuple[Game, int, int],
    *sub_policies: Callable[[Game, int, int], Optional[int]],
) -> int:
    """
    Chains multiple sub policies using the following pattern: a sub policy that return a None value should be ignored.
    """
    return next(
        move
        for sub_policy in sub_policies
        if (move := sub_policy(*args)) is not None
    )


def board_fullness(board: Board) -> Tuple[int, int]:
    """
    Finds the proportion of each side of the board that contains dices.
    """
    return (
        sum(len(col) for col in board["grids"][0]) / board["size"] ** 2,
        sum(len(col) for col in board["grids"][1]) / board["size"] ** 2,
    )
