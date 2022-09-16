import logging
from typing import Literal, Tuple

from .data_structures import Board, Game


def print_board(
    board: Board, player_names: Tuple[str, str] = ("Julien", "Aubin")
) -> None:
    """
    Prints the content of a board (empty cells are indicated with an X).
    """
    separation_line = (board["size"] * 4 - 1) * "-"
    for player_idx in range(2):
        logging.info(
            f"\n{player_names[player_idx]}'s side of the board\n{separation_line}"
        )
        for line in range(board["size"]):
            logging.info(
                " "
                + " | ".join(
                    str(board["grids"][player_idx][col][line])
                    if line < len(board["grids"][player_idx][col])
                    else "X"
                    for col in range(board["size"])
                )
            )
    logging.info(f"{separation_line}\n")


def print_scores(game: Game) -> None:
    """
    Prints the scoreboard.
    """
    first_line = f"{game['player_names'][0]}'s score: {game['player_scores'][0]}"
    second_line = f"{game['player_names'][1]}'s score: {game['player_scores'][1]}"
    logging.info(
        f"{(max(len(first_line), len(second_line)) - 12)// 2 * '-'}"
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
