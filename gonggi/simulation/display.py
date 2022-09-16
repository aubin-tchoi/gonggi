import logging
from typing import Literal

from .data_structures import Board, Game


def print_board(
    board: Board, first_player_name: str = "Julien", second_player_name: str = "Aubin"
) -> None:
    """
    Prints the content of a board (empty cells are indicated with an X).
    """
    separation_line = (board["size"] * 4 - 1) * "-"
    logging.info(f"\n{first_player_name}'s side of the board\n{separation_line}")
    for line in range(board["size"]):
        logging.info(
            " "
            + " | ".join(
                str(board["first_player_grid"][col][line])
                if line < len(board["first_player_grid"][col])
                else "X"
                for col in range(board["size"])
            )
        )
    logging.info(
        f"{separation_line}\n\n{second_player_name}'s side of the board\n{separation_line}"
    )
    for line in range(board["size"]):
        logging.info(
            " "
            + " | ".join(
                str(board["second_player_grid"][col][line])
                if line < len(board["second_player_grid"][col])
                else "X"
                for col in range(board["size"])
            )
        )
    logging.info(f"{separation_line}\n")


def print_scores(game: Game) -> None:
    """
    Prints the scoreboard.
    """
    first_line = f"{game['first_player_name']}'s score: {game['first_player_score']}"
    second_line = f"{game['second_player_name']}'s score: {game['second_player_score']}"
    logging.info(
        f"{(max(len(first_line), len(second_line)) - 12)// 2 * '-'}"
        f" SCOREBOARD "
        f"{(max(len(first_line), len(second_line)) - 12) // 2 * '-'}"
    )
    logging.info(f"{game['first_player_name']}'s score: {game['first_player_score']}")
    logging.info(f"{game['second_player_name']}'s score: {game['second_player_score']}")
    logging.info(f"{max(len(first_line), len(second_line)) * '-'}\n")


def print_game_info(game: Game) -> None:
    """
    Prints some information relative to the progression of a game.
    """
    print_board(game["board"], game["first_player_name"], game["second_player_name"])
    print_scores(game)


def print_winner(game: Game) -> Literal["first", "second", "tie"]:
    """
    Prints a special message for the winner.
    """
    if game["first_player_score"] > game["second_player_score"]:
        logging.info(f"{game['first_player_name']} won, congratulations!")
        return "first"
    elif game["second_player_score"] > game["first_player_score"]:
        logging.info(f"{game['second_player_name']} won, congratulations!")
        return "second"
    else:
        logging.info(
            f"We have a tie between {game['first_player_name']} and {game['second_player_name']}."
        )
        return "tie"