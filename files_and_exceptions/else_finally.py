import time

class GameSession:
    """Manage a game session with guaranteed cleanup."""

    def __init__(self, player_name):
        self.player_name = player_name
        self.started = False
        self.score = 0

    def start(self):
        """Start the session."""
        print(f"🎮 Starting session for {self.player_name}...")
        self.started = True
        self.start_time = time.time()

    def play(self):
        """Simulate gameplay."""
        if not self.started:
            raise RuntimeError("Session not started!")

        print(f"🎯 {self.player_name} is playing...")
        self.score += 100

        # Simulate random error
        import random
        if random.random() < 0.3:  # 30% chance
            raise RuntimeError("Game crashed! (Mia pressed wrong button 😏)")

    def end(self):
        """End the session (cleanup)."""
        if self.started:
            duration = time.time() - self.start_time
            print(f"🏁 Session ended for {self.player_name}")
            print(f"   Score: {self.score}")
            print(f"   Duration: {duration:.2f}s")
            self.started = False

def play_game(player_name):
    """Play a game with guaranteed cleanup."""
    session = GameSession(player_name)

    try:
        session.start()

        # Play a few rounds
        for round_num in range(3):
            print(f"\n--- Round {round_num + 1} ---")
            session.play()
            time.sleep(0.5)

        print(f"\n✅ Game completed successfully!")

    except RuntimeError as e:
        print(f"\n❌ Error occurred: {e}")

    finally:
        # ALWAYS cleanup, even if game crashed
        session.end()
        print("🧹 Session cleanup complete!")

# Play
play_game("Ahad")
