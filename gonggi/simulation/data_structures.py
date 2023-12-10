"""
This module defines the main data structures used for simulation.
They are typed using TypedDicts to allow for transpilation using Pydantic in case a TypeScript front-end is developed.
"""
from typing import TypedDict


class Board(TypedDict):
    """
    Class that stores the information relative to the values placed on the board by each player.
    """

    size: int
    grids: tuple[list[list[int]], list[list[int]]]


class Game(TypedDict):
    """
    Class that stores the information relative to a game.
    """

    # number of sides on the die.
    n_sides: int
    board: Board

    player_names: tuple[str, str]
    player_scores: tuple[int, int]
