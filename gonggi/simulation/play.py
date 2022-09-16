import logging
from random import randint
from typing import Callable, List

from .cost import compute_scores
from .data_structures import Game


def is_column_not_full(size: int, column: List[int]) -> bool:
    """
    Finds out whether a column can receive an additional value or not.
    """
    return len(column) < size


def play_turn(
    game: Game,
    policy: Callable[[Game, int], int],
    is_first_player: bool = True,
    remove_deletion: bool = False,
) -> None:
    """
    Plays a turn of the game by:
    - rolling a die
    - letting the player choose where to put it according to his policy
    - placing the die and deleting the opponent's dices if applicable
    """
    player_name = game["player_names"][not int(is_first_player)]
    grid = game["board"]["grids"][not int(is_first_player)]

    # roll a dice
    dice_value = randint(1, game["n_sides"])
    logging.info(f"{player_name} rolled a {dice_value}.")

    # choose the column
    move = policy(game, dice_value)
    while not (is_value_in_range := 0 <= move < len(grid)) or not is_column_not_full(
        game["board"]["size"], grid[move]
    ):
        logging.warning(
            f"Column {move} is full, playing again."
            if is_value_in_range
            else "Incorrect value passed (not the index of a column), retrying."
        )
        exit(1)
        move = policy(game, dice_value)

    # place the dice
    grid[move].append(dice_value)
    logging.info(f"{player_name} played on column {move}.")

    if not remove_deletion:
        # delete the opponent's dices
        delete_dices(dice_value, move, game["board"]["grids"][int(is_first_player)])


def delete_dices(
    dice_added: int,
    column_added: int,
    grid: List[List[int]],
) -> None:
    """
    Deletes the dices with a certain value in a column of one of the two grids.
    """
    logging.debug(f"Popping dices with value {dice_added} from column {column_added}.")

    for j in range(len(grid[column_added]) - 1, -1, -1):
        if grid[column_added][j] == dice_added:
            logging.info(f"Removing a dice in row {j} with value {dice_added}.")
            grid[column_added].pop(j)


def update_scores(game: Game) -> None:
    """
    Updates the score of each player.
    """
    game["player_scores"] = compute_scores(game["board"])
