def get_full_name(first, last, middle=''):
    """Return a formatted full name."""
    parts = [first]
    if middle:
        parts.append(middle)
    parts.append(last)
    return ' '.join(parts)
