# gonggi

A dice game of risk and reward.

You will find here the rules and the implementation of a simulator for a 2-players dice game.

## How to play

- The game is played on a board made of two n x n grids, one for each player.
- A player's score is the total of all the dice currently placed on his side of the board.
- The players take turn by rolling a dice and placing it on one of the n columns of his side of the board.
- The game ends when one of the two boards is full, the winner is the player with the highest score.

There are two additional behaviors to this game that are described below.

### Match dice

When dice of the same number are placed in the same column, multiply their values.

More precisely, a double amounts to 4 times the value of the dice, and a triple to 9 times.

### Destroy opponent

Destroy your opponent's dice by matching yours to theirs.

> The game was initially designed to be played with a six-sided dice and with n equal to 3.
