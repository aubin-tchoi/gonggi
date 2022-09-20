# You can choose the policies here
from .base_policies import policy_cli, apply_to_player
from .policies import stack_first_then_fill as first_player_policy
from .policies import stack_first_then_fill as second_player_policy
