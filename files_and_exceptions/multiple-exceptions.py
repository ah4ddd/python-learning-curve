def read_file_safely(filename):
    """Read file with comprehensive error handling."""
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
        error_type = type(e).__name__
        print(f"❌ Cannot read file: {error_type}")
        print(f"   {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

content = read_file_safely("data.txt")
