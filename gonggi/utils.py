from data_structures import Board, Game


def print_board(
    board: Board, first_player_name: str = "Julien", second_player_name: str = "Aubin"
) -> None:
    print(f"\n{first_player_name}'s side of the board")
    # TODO: n - depends on the size of the board
    print("------------------------------------------")
    for line in range(board["size"]):
        print(
            " | ".join(
                str(board["first_player_grid"][col][line])
                if line < len(board["first_player_grid"][col])
                else "X"
                for col in range(board["size"])
            )
        )
    print("------------------------------------------\n")
    print(f"{second_player_name}'s side of the board")
    print("------------------------------------------")
    for line in range(board["size"]):
        print(
            " | ".join(
                str(board["second_player_grid"][col][line])
                if line < len(board["second_player_grid"][col])
                else "X"
                for col in range(board["size"])
            )
        )
    print("------------------------------------------\n")


def print_scores(game: Game) -> None:
    first_line = f"{game['first_player_name']}'s score: {game['first_player_score']}"
    second_line = f"{game['second_player_name']}'s score: {game['second_player_score']}"
    print(
        f"{(max(len(first_line), len(second_line)) - 12)// 2 * '-'}"
        f" SCOREBOARD "
        f"{(max(len(first_line), len(second_line)) - 12) // 2 * '-'}"
    )
    print(f"{game['first_player_name']}'s score: {game['first_player_score']}")
    print(f"{game['second_player_name']}'s score: {game['second_player_score']}")
    print(f"{max(len(first_line), len(second_line)) * '-'}\n")


def print_game_info(game: Game) -> None:
    print_board(game["board"], game["first_player_name"], game["second_player_name"])
    print_scores(game)


def print_winner(game: Game) -> None:
    if game["first_player_score"] > game["second_player_score"]:
        print(f"{game['first_player_name']} won, congratulations!")
    elif game["second_player_score"] > game["first_player_score"]:
        print(f"{game['second_player_name']} won, congratulations!")
    else:
        print(
            f"We have a tie between {game['first_player_name']} and {game['second_player_name']}."
        )
