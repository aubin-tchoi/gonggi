from typing import List

from gonggi import Game, print_board


def policy_template(game: Game, dice_value: int) -> int:
    pass


def policy_cli(game: Game, dice_value: int) -> int:
    print_board(game["board"])
    input_message = f"You rolled a {dice_value}, in which column do you want to put it? "
    while (user_input := int(input(input_message))) > game["board"]["size"]:
        print("Incorrect value passed, please try again.")
    return user_input


def is_column_not_full(size: int, grid: List[List[int]], move: int) -> bool:
    return len(grid[move]) < size
