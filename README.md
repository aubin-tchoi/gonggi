# gonggi

A die game of risk and reward.

You will find here the rules and the implementation of a simulator for a 2-players dice game.

> Note that this game has nothing to do with the game of gonggi, which is a traditional Korean game.
> 
> We do not know the actual name of the game implemented here though.

## How to play

- The game is played on a board made of two n x n grids, one for each player.
- A player's score is the total of all the dice currently placed on his side of the board.
- The players take turn by rolling a die and placing it on one of the n columns of his side of the board.
- The game ends when one of the two boards is full, the winner is the player with the highest score.

> The game was initially designed to be played with a six-sided dice and with n equal to 3.

There are two additional behaviors to this game that are described below.

### Match dice

When dice of the same number are placed in the same column, multiply their values.

More precisely, k similar dices in a same column amount to k ** 2 the value of the dice.

### Destroy opponent

Destroy your opponent's dice by matching yours to theirs.

If a player places a die of value x in column j of his side of the board, all dice with the same value are removed from\
column j of his opponent's side of the board.

## Implementation

To play the game, run the `__main__.py` script.

Run the script with the flag `--help` for information on the arguments of the script.

The policies used by each player are also specified in this file when running the game.

### Adding a policy

You can add your own policy in files `first_player_policy.py` and `second_player_policy.py`.

To do so, use the template in `base_policies.py`.
