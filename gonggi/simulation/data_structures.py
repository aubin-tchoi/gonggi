from typing import List, Tuple, TypedDict


class Board(TypedDict):
    """
    Class that stores the information relative to the values placed on the board by each player.
    """

    size: int
    grids: Tuple[List[List[int]], List[List[int]]]


class Game(TypedDict):
    """
    Class that stores the information relative to a game.
    """

    # number of sides on the die.
    n_sides: int
    board: Board

    player_names: Tuple[str, str]
    player_scores: Tuple[int, int]
