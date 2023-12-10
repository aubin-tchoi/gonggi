import logging

from gonggi.simulation import (
    Board,
    Game,
    Policy,
    is_column_not_full,
    play_turn,
    print_half_board,
    update_scores,
)


def instantiate_new_single_player_game(
    board_size: int,
    n_sides: int,
) -> Game:
    """
    Creates a new game.

    Args:
        board_size: Size of the board (each player will play on a board_size x board_size grid).
        n_sides: Number of sides on the die.

    Returns:
        The newly created game.
    """
    logging.info(
        f"Launching a new game with a board of size {board_size} using a {n_sides}-sided die.\n"
    )
    return Game(
        n_sides=n_sides,
        board=Board(
            size=board_size,
            grids=([[] for _ in range(board_size)], [[] for _ in range(board_size)]),
        ),
        player_scores=(0, 0),
        player_names=("You", ""),
    )


def is_half_board_not_full(game: Game) -> bool:
    """
    Finds out if there is room left on both players' sides of the grid.
    """
    return any(
        is_column_not_full(game["board"]["size"], game["board"]["grids"][0][col])
        for col in range(game["board"]["size"])
    )


def run_single_player_game(game: Game, policy: Policy) -> int:
    """
    Plays the game until one side of the board is full.
    """
    while is_half_board_not_full(game):
        play_turn(game, policy)
        update_scores(game)
        logging.info("Your board:")
        print_half_board(game["board"])
        logging.info(f"Your score: {game['player_scores'][0]:>2}\n")

    return game["player_scores"][0]
