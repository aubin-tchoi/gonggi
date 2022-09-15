from typing import Tuple, List, DefaultDict

from data_structures import Board


def find_player_score(size: int, player_grid: List[DefaultDict[int, int]]) -> int:
    """
    Finds out the score associated with a grid.
    """
    return sum(
        dice * occurrences**2
        for col in range(size)
        for dice, occurrences in player_grid[col].items()
    )


def compute_scores(board: Board) -> Tuple[int, int]:
    """
    Computes the scores of the two players.
    """
    return (
        find_player_score(board["size"], board["first_player_grid"]),
        find_player_score(board["size"], board["second_player_grid"]),
    )
