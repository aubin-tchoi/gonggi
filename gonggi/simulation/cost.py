from typing import Tuple, List

from .data_structures import Board


def find_player_score(size: int, player_grid: List[List[int]]) -> int:
    """
    Finds out the score associated with a grid.
    """
    return sum(
        dice * player_grid[col].count(dice) ** 2
        for col in range(size)
        for dice in set(player_grid[col])
    )


def compute_scores(board: Board) -> Tuple[int, int]:
    """
    Computes the scores of the two players.
    """
    return (
        find_player_score(board["size"], board["grids"][0]),
        find_player_score(board["size"], board["grids"][1]),
    )
