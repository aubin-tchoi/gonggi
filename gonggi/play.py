from random import randint
from typing import Callable, List

from cost import compute_scores
from data_structures import Game
from utils import print_board


def is_column_not_full(size: int, grid: List[List[int]], move: int) -> bool:
    return len(grid[move]) < size


def play_turn(
    game: Game,
    first_player_policy: Callable[[Game, int], int],
    second_player_policy: Callable[[Game, int], int],
) -> None:
    # roll a dice
    first_dice_value = randint(1, game["n_sides"])
    # choose the column
    first_player_move = first_player_policy(game, first_dice_value)
    while not is_column_not_full(
        game["board"]["size"], game["board"]["first_player_grid"], first_player_move
    ):
        print(f"Column {first_player_move} is full, retrying.")
        first_player_move = first_player_policy(game, first_dice_value)

    # place the dice
    game["board"]["first_player_grid"][first_player_move].append(first_dice_value)

    # delete the opponent's dices
    delete_dices(
        first_dice_value, first_player_move, game["board"]["second_player_grid"]
    )

    second_dice_value = randint(1, game["n_sides"])
    second_player_move = second_player_policy(game, second_dice_value)
    while not is_column_not_full(
        game["board"]["size"], game["board"]["second_player_grid"], second_player_move
    ):
        print(f"Column {second_player_move} is full, retrying.")
        second_player_move = second_player_policy(game, second_dice_value)

    game["board"]["second_player_grid"][second_player_move].append(second_dice_value)
    delete_dices(
        second_dice_value, second_player_move, game["board"]["first_player_grid"]
    )


def delete_dices(
    dice_added: int, column_added: int, grid: List[List[int]], verbose: bool = True
) -> None:
    if verbose:
        print(f"Popping dices with value {dice_added} from column {column_added}.")

    for j in range(len(grid[column_added]) - 1, -1, -1):
        if grid[column_added][j] == dice_added:
            if verbose:
                print(f"Found a dice in row {j}, popping it.")
            grid[column_added].pop(j)


def update_scores(game: Game) -> None:
    game["first_player_score"], game["second_player_score"] = compute_scores(
        game["board"]
    )