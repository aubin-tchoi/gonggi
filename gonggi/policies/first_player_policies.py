from gonggi.simulation.data_structures import Game
from gonggi.simulation.play import is_column_not_full


# noinspection PyUnusedLocal
def left_to_right(game: Game, dice_value: int) -> int:
    """
    Choosing the first available column.
    Can be used to benchmark a policy, any policy should be better than this one.
    """
    return next(
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(game["board"]["size"], game["board"]["grids"][0][col])
    )


def stack_first_then_fill(game: Game, dice_value: int) -> int:
    # stacking the dice if possible
    for col in range(game["board"]["size"]):
        if dice_value in set(game["board"]["grids"][0][col]) and is_column_not_full(
            game["board"]["size"], game["board"]["grids"][0][col]
        ):
            return col

    # then choosing an empty column if there is one
    for col in range(game["board"]["size"]):
        if len(game["board"]["grids"][0][col]) == 0:
            return col

    # finally choosing the first non-full column
    return next(
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(game["board"]["size"], game["board"]["grids"][0][col])
    )


def fill_first_then_stack(game: Game, dice_value: int) -> int:
    # choosing an empty column if there is one
    for col in range(game["board"]["size"]):
        if len(game["board"]["grids"][0][col]) == 0:
            return col

    # stacking the dice if possible
    for col in range(game["board"]["size"]):
        if dice_value in set(game["board"]["grids"][0][col]) and is_column_not_full(
            game["board"]["size"], game["board"]["grids"][0][col]
        ):
            return col

    # finally choosing the first non-full column
    return next(
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(game["board"]["size"], game["board"]["grids"][0][col])
    )

def counter(game: Game, dice_value: int) -> int:
    for col in range(game["board"]["size"]):
        if dice_value in game["board"][col]:
           return col

    return next(
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(game["board"]["size"], game["board"]["grids"][1][col])
    )
