import enum


class GameStatus(enum.Enum):
    """An enum to represent the various states a game can be in.

    Arguments:
        enum {int} -- Inherits from Enum class to allow Enum representation of game states.
    """

    game_in_progress = 0
    game_won = 1
    game_lost = 2
