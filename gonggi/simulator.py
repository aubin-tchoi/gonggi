from typing import Callable

from data_structures import Game, Board
from play import is_column_not_full, play_turn, update_scores
from utils import print_game_info, print_winner


def instantiate_new_game(
    board_size: int,
    n_sides: int,
    first_player_name: str,
    second_player_name: str,
) -> Game:
    return Game(
        n_sides=n_sides,
        board=Board(
            size=board_size,
            first_player_grid=[[] for _ in range(board_size)],
            second_player_grid=[[] for _ in range(board_size)],
        ),
        first_player_score=0,
        second_player_score=0,
        first_player_name=first_player_name,
        second_player_name=second_player_name,
    )


def run_game(
    game: Game,
    first_player_policy: Callable[[Game, int], int],
    second_player_policy: Callable[[Game, int], int],
) -> None:
    while any(
        is_column_not_full(
            game["board"]["size"], game["board"]["first_player_grid"], col
        )
        for col in range(game["board"]["size"])
    ) and any(
        is_column_not_full(
            game["board"]["size"], game["board"]["second_player_grid"], col
        )
        for col in range(game["board"]["size"])
    ):
        play_turn(game, first_player_policy, second_player_policy)
        update_scores(game)
        print_game_info(game)
    print_winner(game)
