__all__ = [
    "instantiate_new_single_player_game",
    "run_single_player_game",
    "instantiate_new_game",
    "run_game",
]

from .single_player_game import (
    instantiate_new_single_player_game,
    run_single_player_game,
)
from .two_players_game import instantiate_new_game, run_game
