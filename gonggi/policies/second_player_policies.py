from gonggi.simulation.data_structures import Game
from gonggi.simulation.play import is_column_not_full


def second_player_naive_policy(game: Game, dice_value: int) -> int:
    for col in range(game["board"]["size"]):
        if dice_value in set(game["board"]["grids"][1][col]) and is_column_not_full(
            game["board"]["size"], game["board"]["grids"][1][col]
        ):
            return col

    for col in range(game["board"]["size"]):
        if len(game["board"]["grids"][1][col]) == 0:
            return col

    return next(
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(game["board"]["size"], game["board"]["grids"][1][col])
    )
