"""
A score policy is a policy that returns a list of scores associated with each column.

Score policies all have the same typing: Callable[[Game, int, int], list[int]],
which allows them to be chained using utils.chain_score_policies.
The length of the list returned should be equal to the number of columns.
"""
from copy import deepcopy

from gonggi.simulation import Game, compute_scores, delete_dices, is_column_not_full


def best_counter(game: Game, player_index: int, dice_value: int) -> list[int]:
    """
    Returns the first column the player can use to delete his opponent's dice if there is one.
    Variant of counter that removes a maximal number of dices.
    """
    return [
        game["board"]["grids"][1 - player_index][col].count(dice_value)
        for col in range(game["board"]["size"])
    ]


def greedy(game: Game, player_index: int, dice_value: int) -> list[int]:
    """
    Greedy algorithm that simulates each move.
    """
    scores = []
    for move in range(game["board"]["size"]):
        if is_column_not_full(
            game["board"]["size"], game["board"]["grids"][player_index][move]
        ):
            # computing the hypothetical score if the player were to do this move
            board_copy = deepcopy(game["board"])
            board_copy["grids"][player_index][move].append(dice_value)
            delete_dices(dice_value, move, board_copy["grids"][1 - player_index])
            updated_scores = compute_scores(board_copy)
            scores.append(
                updated_scores[player_index] - updated_scores[1 - player_index]
            )
        else:
            scores.append(-game["board"]["size"] ** 3)

    return scores
