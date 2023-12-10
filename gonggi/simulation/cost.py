from .data_structures import Board


def find_player_score(
    size: int, player_grid: list[list[int]], remove_stacking: bool = False
) -> int:
    """
    Finds out the score associated with a grid.
    """
    return (
        sum(dice for col in range(len(player_grid)) for dice in player_grid[col])
        if remove_stacking
        else sum(
            dice * player_grid[col].count(dice) ** 2
            for col in range(size)
            for dice in set(player_grid[col])
        )
    )


def compute_scores(board: Board) -> tuple[int, int]:
    """
    Computes the scores of the two players.
    """
    return (
        find_player_score(board["size"], board["grids"][0]),
        find_player_score(board["size"], board["grids"][1]),
    )
