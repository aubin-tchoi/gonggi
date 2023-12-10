import logging
from random import randint

from .cost import compute_scores
from .data_structures import Game, Policy


def is_column_not_full(size: int, column: list[int]) -> bool:
    """
    Finds out whether a column can receive an additional value or not.
    """
    return len(column) < size


def play_turn(
    game: Game,
    policy: Policy,
    player_index: int = 0,
    remove_deletion: bool = False,
) -> None:
    """
    Plays a turn of the game by:
    - rolling a die
    - letting the player choose where to put it according to his policy
    - placing the die and deleting the opponent's dices if applicable
    """
    player_name = game["player_names"][player_index]
    grid = game["board"]["grids"][player_index]

    # roll a die
    dice_value = randint(1, game["n_sides"])
    logging.info(f"{player_name} rolled a {dice_value}.")

    # choose the column
    move = policy(game, player_index, dice_value)
    n_tries = 0
    while not (is_value_in_range := 0 <= move < len(grid)) or not is_column_not_full(
        game["board"]["size"], grid[move]
    ):
        logging.warning(
            f"Column {move} is full, playing again."
            if is_value_in_range
            else "Incorrect value passed (not the index of a column), retrying."
        )
        move = policy(game, player_index, dice_value)
        if n_tries > 100:
            raise RuntimeError("There is an issue with the policy.")
        n_tries += 1

    # place the dice
    grid[move].append(dice_value)
    logging.info(f"{player_name} played on column {move}.")

    if not remove_deletion:
        # delete the opponent's dices
        delete_dices(dice_value, move, game["board"]["grids"][1 - player_index])


def delete_dices(
    dice_added: int,
    column_added: int,
    grid: list[list[int]],
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
