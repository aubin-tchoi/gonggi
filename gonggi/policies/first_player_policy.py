from gonggi import Game, is_column_not_full


def first_player_naive_policy(game: Game, dice_value: int) -> int:
    for col in range(game["board"]["size"]):
        if dice_value in set(
            game["board"]["first_player_grid"][col]
        ) and is_column_not_full(
            game["board"]["size"], game["board"]["first_player_grid"], col
        ):
            return col

    for col in range(game["board"]["size"]):
        if len(game["board"]["first_player_grid"][col]) == 0:
            return col

    return next(
        col
        for col in range(game["board"]["size"])
        if is_column_not_full(
            game["board"]["size"], game["board"]["first_player_grid"], col
        )
    )
