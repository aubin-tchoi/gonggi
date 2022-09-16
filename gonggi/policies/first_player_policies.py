from gonggi.simulation.data_structures import Game
from gonggi.simulation.play import is_column_not_full


def first_player_naive_policy(game: Game, dice_value: int) -> int:
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
