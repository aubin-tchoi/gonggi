from typing import Tuple, List

from data_structures import Board


def find_nb_occurrences(column: List[int], dice_value: int) -> int:
    return len(list(filter(lambda value: value == dice_value, column)))


def find_player_score(size: int, player_grid: List[List[int]]) -> int:
    total_points = 0
    for col in range(size):
        for dice in set(player_grid[col]):
            nb_occurrences = find_nb_occurrences(player_grid[col], dice)
            total_points += nb_occurrences**2 * dice

    return total_points


def compute_scores(board: Board) -> Tuple[int, int]:
    return (
        find_player_score(board["size"], board["first_player_grid"]),
        find_player_score(board["size"], board["second_player_grid"]),
    )
