from typing import Tuple, List

from data_structures import Board


def find_nb_occurrences(column: List[int], dice_value: int) -> int:
    return len(list(filter(lambda value: value == dice_value, column)))


def find_player_score(size: int, player_grid: List[List[int]]) -> int:
    return sum(
        dice * find_nb_occurrences(player_grid[col], dice) ** 2
        for col in range(size)
        for dice in set(player_grid[col])
    )


def compute_scores(board: Board) -> Tuple[int, int]:
    return (
        find_player_score(board["size"], board["first_player_grid"]),
        find_player_score(board["size"], board["second_player_grid"]),
    )
