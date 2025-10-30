def analyze_text(text):
    """
    Analyzes text, returns various stats
    Returns (word_count, char_count, is_long, first_word)
    """
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    is_long = word_count > 50
    first_word = words[0] if words else ""

    return word_count, char_count, is_long, first_word
    # Returns: int, int, bool, str — all different types!

# Use it:
text = "Python is amazing and I'm learning it in 20 days!"
w_count, c_count, is_long, first = analyze_text(text)

print(f"Words: {w_count}")        # 10
print(f"Characters: {c_count}")   # 50
print(f"Long text?: {is_long}")   # False
print(f"First word: {first}")     # Python
