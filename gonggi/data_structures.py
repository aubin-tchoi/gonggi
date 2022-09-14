from typing import TypedDict, List


class Board(TypedDict):
    """
    Class that stores the information relative to the values placed on the board by each player.
    """
    size: int
    first_player_grid: List[List[int]]
    second_player_grid: List[List[int]]


class Game(TypedDict):
    """
    Class that stores the information relative to a game.
    """
    # number of sides on the die.
    n_sides: int
    board: Board

    first_player_name: str
    second_player_name: str

    first_player_score: int
    second_player_score: int
