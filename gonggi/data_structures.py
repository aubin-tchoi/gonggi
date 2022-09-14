from typing import TypedDict, List


class Board(TypedDict):
    size: int
    first_player_grid: List[List[int]]
    second_player_grid: List[List[int]]


class Game(TypedDict):
    n_sides: int
    board: Board
    first_player_name: str
    second_player_name: str
    first_player_score: int
    second_player_score: int
