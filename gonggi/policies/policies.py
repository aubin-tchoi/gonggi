from random import randint

from gonggi.simulation import Game, is_column_not_full, print_board

from .score_policies import best_counter, greedy
from .sub_policies import counter, first_empty_column, first_non_full_column, stack
from .utils import chain_score_policies, chain_sub_policies, sub_policy_to_score_policy


def policy_cli(game: Game, player_index: int, dice_value: int) -> int:
    """
    Policy that consists in asking for user input.
    """
    print_board(game["board"], game["player_names"])
    return int(
        input(
            f"{game['player_names'][player_index]} rolled a {dice_value}, in which column do you want to put it? "
        )
    )


def left_to_right(game: Game, player_index: int, dice_value: int) -> int:
    """
    Choosing the first available column.
    Can be used to benchmark a policy, any policy should be better than this one.
    """
    return first_non_full_column(game, player_index, dice_value)


# noinspection PyUnusedLocal
def random_choice(game: Game, player_index: int, dice_value: int) -> int:
    """
    Choosing a random column.
    Be careful when using this whilst using a random seed for the dice rolls as the two would interfere.
    """
    admissible_columns = [
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(
            game["board"]["size"], game["board"]["grids"][player_index][col]
        )
    ]
    return admissible_columns[randint(0, len(admissible_columns) - 1)]


def stack_first_then_fill(game: Game, player_index: int, dice_value: int) -> int:
    return chain_sub_policies(
        (game, player_index, dice_value),
        stack,
        first_empty_column,
        first_non_full_column,
    )


def fill_first_then_stack(game: Game, player_index: int, dice_value: int) -> int:
    return chain_sub_policies(
        (game, player_index, dice_value),
        first_empty_column,
        stack,
        first_non_full_column,
    )


def counter_then_stack(game: Game, player_index: int, dice_value: int) -> int:
    return chain_sub_policies(
        (game, player_index, dice_value),
        counter,
        stack,
        first_empty_column,
        first_non_full_column,
    )


def counter_then_fill(game: Game, player_index: int, dice_value: int) -> int:
    return chain_sub_policies(
        (game, player_index, dice_value),
        counter,
        first_empty_column,
        stack,
        first_non_full_column,
    )


def greedy_then_first_non_full(game: Game, player_index: int, dice_value: int) -> int:
    return chain_score_policies(
        (game, player_index, dice_value),
        greedy,
        sub_policy_to_score_policy(first_non_full_column),
    )


def greedy_then_fill(game: Game, player_index: int, dice_value: int) -> int:
    return chain_score_policies(
        (game, player_index, dice_value),
        greedy,
        sub_policy_to_score_policy(first_empty_column),
    )


def greedy_then_counter_then_fill(
    game: Game, player_index: int, dice_value: int
) -> int:
    return chain_score_policies(
        (game, player_index, dice_value),
        greedy,
        best_counter,
        sub_policy_to_score_policy(first_empty_column),
    )
