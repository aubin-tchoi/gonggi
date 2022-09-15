import logging
from random import randint
from typing import Callable, List, DefaultDict

from cost import compute_scores
from data_structures import Game


def is_column_not_full(size: int, column: DefaultDict[int, int]) -> bool:
    """
    Finds out whether a column can receive an additional value or not.
    """
    return sum(column.values()) < size


def play_turn(
    game: Game,
    first_player_policy: Callable[[Game, int], int],
    second_player_policy: Callable[[Game, int], int],
) -> None:
    """
    Plays a turn of the game by:
    - rolling a die
    - letting the first player choose where to put it according to his policy
    - placing the die and deleting the opponent's dices if applicable
    and repeating these steps for the second player.
    """
    # roll a dice
    first_dice_value = randint(1, game["n_sides"])
    logging.info(f"{game['first_player_name']} rolled a {first_dice_value}.")

    # choose the column
    first_player_move = first_player_policy(game, first_dice_value)
    while not is_column_not_full(
        game["board"]["size"], game["board"]["first_player_grid"][first_player_move]
    ):
        logging.info(f"Column {first_player_move} is full, playing again.")
        first_player_move = first_player_policy(game, first_dice_value)

    # place the dice
    game["board"]["first_player_grid"][first_player_move][first_dice_value] += 1
    logging.info(f"{game['first_player_name']} plays on column {first_player_move}.")

    # delete the opponent's dices
    delete_dices(
        first_dice_value, first_player_move, game["board"]["second_player_grid"]
    )

    second_dice_value = randint(1, game["n_sides"])
    logging.info(f"{game['second_player_name']} rolled a {second_dice_value}.")

    second_player_move = second_player_policy(game, second_dice_value)
    while not is_column_not_full(
        game["board"]["size"], game["board"]["second_player_grid"][second_player_move]
    ):
        logging.info(f"Column {second_player_move} is full, retrying.")
        second_player_move = second_player_policy(game, second_dice_value)

    game["board"]["second_player_grid"][second_player_move][second_dice_value] += 1
    logging.info(f"{game['second_player_name']} plays on column {second_player_move}.")

    delete_dices(
        second_dice_value, second_player_move, game["board"]["first_player_grid"]
    )


def delete_dices(
    dice_added: int,
    column_added: int,
    grid: List[DefaultDict[int, int]],
) -> None:
    """
    Deletes the dices with a certain value in a column of one of the two grids.
    """
    logging.debug(f"Popping dices with value {dice_added} from column {column_added}.")
    if dice_added in grid[column_added]:
        logging.info(
            f"Removing {grid[column_added][dice_added]} dice in column {column_added} with value {dice_added}."
        )
        grid[column_added].pop(dice_added)


def update_scores(game: Game) -> None:
    """
    Updates the score of each player.
    """
    game["first_player_score"], game["second_player_score"] = compute_scores(
        game["board"]
    )
