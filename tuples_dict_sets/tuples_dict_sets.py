# Example 1: Basic usage with default space padding
text1 = "Python"
centered_text1 = text1.center(10)
print(centered_text1)

# Example 2: Using a custom fill character
text2 = "Hello"
centered_text2 = text2.center(15, '*')
print(centered_text2)

# Example 3: Width less than string length
text3 = "Programming"
centered_text3 = text3.center(15)
print(centered_text3)

# Example 4: Width equal to string length
text4 = "Code"
centered_text4 = text4.center(8, '-')
print(centered_text4)
