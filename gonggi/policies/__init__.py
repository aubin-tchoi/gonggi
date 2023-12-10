# you can choose the policies here
from .base_policies import apply_to_player, policy_cli
from .policies import (
    greedy_then_fill as second_player_policy,
    stack_first_then_fill as first_player_policy,
    stack_first_then_fill as single_player_policy,
)
