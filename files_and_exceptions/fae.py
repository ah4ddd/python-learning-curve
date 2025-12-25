# Base exception for all game errors
class GameError(Exception):
    """Base exception for game-related errors."""
    pass

# Specific game errors (inherit from GameError)
class InvalidMoveError(GameError):
    """Raised when move is invalid."""
    pass

class GameOverError(GameError):
    """Raised when game is over."""
    pass

class PlayerNotFoundError(GameError):
    """Raised when player doesn't exist."""
    pass

# Use them
def make_move(player, move):
    if not player:
        raise PlayerNotFoundError("Player not found!")
    if not is_valid_move(move):
        raise InvalidMoveError(f"Move '{move}' is not valid!")
    # Make move...

def is_valid_move(move):
    return move in ["up", "down", "left", "right"]

# Catch specific or general
try:
    make_move(None, "up")
except PlayerNotFoundError as e:
    print(f"❌ Player error: {e}")
except InvalidMoveError as e:
    print(f"❌ Move error: {e}")
except GameError as e:
    print(f"❌ Game error: {e}")  # Catches ANY game error!
