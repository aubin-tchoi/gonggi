"""
This module defines the main data structures used for simulation.
They are typed using TypedDicts to allow for transpilation using Pydantic in case a TypeScript front-end is developed.
"""
from typing import Protocol, TypedDict


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


class Policy(Protocol):
    def __call__(self, game: Game, player_index: int, dice_value: int) -> int:
        """
        Typing interface for ready-to-use policies.
        A policy will always take these three arguments in this order.

        Args:
            game: The state of the game.
            You can retrieve the values on the board here.
            player_index: The index of the player who plays (0 for the first player, 1 for the second one).
            This argument is required for the policy to understand which side it plays for since it has full information
            on the state of the game.
            dice_value: The value of the die to place on the board.

        Returns:
            The index of the column to play on.
        """
        ...
