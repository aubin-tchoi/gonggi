import logging
from typing import Literal

from .data_structures import Board, Game


def print_grid(size: int, grid: list[list[int]]):
    """
    Prints a grid with 'X' for empty cells.
    """
    for line in range(size):
        logging.info(
            " "
            + " | ".join(
                str(grid[col][line]) if line < len(grid[col]) else "X"
                for col in range(size)
            )
        )


def print_board(board: Board, player_names: tuple[str, str]) -> None:
    """
    Prints the content of a board (empty cells are indicated with an X).
    """
    separation_line = (board["size"] * 4 - 1) * "-"
    logging.info("")
    for player_idx in range(2):
        logging.info(
            f"{player_names[player_idx]}'s side of the board\n{separation_line}"
        )
        print_grid(board["size"], board["grids"][player_idx])
        logging.info(f"{separation_line}")


def print_half_board(board: Board) -> None:
    """
    Prints the content of the first half of a board (useful for single player game).
    """
    separation_line = (board["size"] * 4 - 1) * "-"
    print_grid(board["size"], board["grids"][0])
    logging.info(f"{separation_line}")


def print_scores(game: Game) -> None:
    """
    Prints the scoreboard.
    """
    first_line = f"{game['player_names'][0]}'s score: {game['player_scores'][0]}"
    second_line = f"{game['player_names'][1]}'s score: {game['player_scores'][1]}"
    logging.info(
        f"\n{(max(len(first_line), len(second_line)) - 12) // 2 * '-'}"
        f" SCOREBOARD "
        f"{(max(len(first_line), len(second_line)) - 12) // 2 * '-'}"
    )
    logging.info(first_line)
    logging.info(second_line)
    logging.info(f"{max(len(first_line), len(second_line)) * '-'}\n")


def print_game_info(game: Game) -> None:
    """
    Prints some information relative to the progression of a game.
    """
    print_board(game["board"], game["player_names"])
    print_scores(game)


def print_winner(game: Game) -> Literal["first", "second", "tie"]:
    """
    Prints a special message for the winner.
    """
    if game["player_scores"][0] > game["player_scores"][1]:
        logging.info(f"{game['player_names'][0]} won, congratulations!")
        return "first"
    elif game["player_scores"][1] > game["player_scores"][0]:
        logging.info(f"{game['player_names'][1]} won, congratulations!")
        return "second"
    else:
        logging.info(f"We have a tie between {' and '.join(game['player_names'])}.")
        return "tie"
