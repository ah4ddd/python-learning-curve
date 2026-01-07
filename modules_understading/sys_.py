import sys

# 1. Validate arguments
if len(sys.argv) != 2:
    sys.stderr.write("Usage: python analyze.py <text>\n")
    sys.exit(1)

# 2. Read input from command line
text = sys.argv[1]

# 3. Do actual work
char_count = len(text)
word_count = len(text.split())

# 4. Output results
sys.stdout.write(f"your text : {text}\n")
sys.stdout.write(f"Characters: {char_count}\n")
sys.stdout.write(f"Words: {word_count}\n")

# 5. Exit successfully
sys.exit(0)
