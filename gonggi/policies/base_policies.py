from gonggi import Game, print_board


def policy_template(game: Game, dice_value: int) -> int:
    """
    A policy will always take these 2 arguments.

    Args:
        game: The state of the game. You can retrieve the values on the board here.
        dice_value: The value of the die to place on the board.

    Returns:
        The index of the column to play on.
    """
    pass


def policy_cli(game: Game, dice_value: int) -> int:
    """
    Policy that consists in asking for user input.
    """
    print_board(game["board"])
    input_message = (
        f"You rolled a {dice_value}, in which column do you want to put it? "
    )
    while (user_input := int(input(input_message))) > game["board"]["size"]:
        print("Incorrect value passed, please try again.")
    return user_input
