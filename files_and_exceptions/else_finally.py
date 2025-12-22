import json

def save_calculation_history(history, filename="history.json"):
    """Save history with guaranteed cleanup."""
    file_handle = None
    temp_filename = filename + ".tmp"  # Temporary file

    try:
        print(f"💾 Saving to {filename}...")

        # Write to temporary file first (safer!)
        file_handle = open(temp_filename, "w")
        json.dump(history, file_handle, indent=4)
        file_handle.close()

        # Rename temp to actual (atomic operation)
        import os
        if os.path.exists(filename):
            os.remove(filename)
        os.rename(temp_filename, filename)

        print(f"✅ Saved successfully!")
        return True

    except IOError as e:
        print(f"❌ Failed to save: {e}")
        return False

    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

    finally:
        # Cleanup: Close file if still open
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("🧹 Closed file handle")

        # Remove temp file if it exists and save failed
        import os
        if os.path.exists(temp_filename):
            try:
                os.remove(temp_filename)
                print("🧹 Cleaned up temporary file")
            except:
                pass  # Cleanup failed, but that's okay

# Test
history = [
    {"user": "Ahad", "a": 10, "operator": "+", "b": 5, "result": 15},
    {"user": "Mia", "a": 20, "operator": "*", "b": 2, "result": 40}
]

save_calculation_history(history)
