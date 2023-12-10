__all__ = ["single_player_policy", "first_player_policy", "second_player_policy"]

# you can choose the policies here
from .policies import greedy_then_fill as second_player_policy
from .policies import stack_first_then_fill as first_player_policy
from .policies import stack_first_then_fill as single_player_policy
