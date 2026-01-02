def get_full_name(first, last, middle=''):
    """Return a formatted full name."""
    if middle:
        return f"{first} {middle} {last}"
    else:
        return f"{first} {last}"
