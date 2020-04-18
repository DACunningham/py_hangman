import enum


class GameStatus(enum.Enum):
    still_playing = 0
    success = 1
    game_over = 2
