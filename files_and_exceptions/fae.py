import time

def connect_to_server(max_attempts=3):
    """Try to connect with retry logic."""
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"🔄 Attempt {attempt}/{max_attempts}...")

            # Simulate connection (replace with real code)
            import random
            if random.random() < 0.7:  # 70% chance of failure
                raise ConnectionError("Server not responding")

            print("✅ Connected successfully!")
            return True

        except (ConnectionError, TimeoutError) as e:
            print(f"❌ {e}")
            if attempt < max_attempts:
                print(f"   Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print(f"   Max attempts reached. Giving up.")
                return False

# Use it
connect_to_server()
