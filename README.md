# gonggi

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

A die game of risk and reward.

You will find here the rules and the implementation of a simulator for a 2-player dice game.

> Note that this game has nothing to do with the game of gonggi, which is a traditional Korean game.
> 
> We do not know the actual name of the game implemented here though.

## Usage

Run the game using `poetry run play_game`, or alternatively without Poetry: `python3 scripts/play_game.py` 
(this project is actually pure Python as detailed [here](#Implementation)).

Doing so will run the game with the policies defined in `gonggi.policies.__init__.py`.

See `poetry run play_game --help` for more information on the script options.

## 📜 Rules of the game

- The game is played on a board made of two n x n grids, one for each player.
- A player's score is the total of all the dice currently placed on his side of the board.
- The players take turn by rolling a die and placing it on one of the n columns of his side of the board.
- The game ends when one of the two boards is full, the winner is the player with the highest score.

> The game was initially designed to be played with a six-sided dice and with n equal to 3.

There are two additional behaviors to this game that are described below.

### 🎲 Match dice

When dice of the same number are placed in the same column, multiply their values.

More precisely, k similar dices in the same column amount to k ** 2 the value of the dice.

### ♟️ Destroy opponent

Destroy your opponent's dice by matching yours to theirs.

If a player places a die of value x in column j of his side of the board, all dice with the same value are removed from
column j of his opponent's side of the board.

## Implementation

This project is written in pure Python (no heavy computation is performed, no need for efficient NumPy-based operations)
and supports Python >= 3.8.
Therefore, the dependencies only contain development tools, and there is no particular need to install a dedicated venv.

### 📦 Dependency management and packaging

Dependencies are managed using `poetry`: https://python-poetry.org/.

To install `poetry` follow the steps in: https://python-poetry.org/docs/.

- The dependencies are listed in a `pyproject.toml` alongside supported ranges of versions for each dependency.
- The exact versions used can be frozen using `poetry lock`, which generated a snapshot in the form of the `poetry.lock`
  file.
- The dependencies can then be installed in a virtualenv (cached under `~/.cache/pypoetry`) by running `poetry install`.

### 🔨 Adding a policy

You can add your own policies in files `first_player_policy.py` and `second_player_policy.py`.

To do so, use the template in `base_policies.py`.
