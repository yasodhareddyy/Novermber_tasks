import re

def isMatch(s, p):
    # Convert '*' to '.*' and '?' to '.'
    p = p.replace('*', '.*').replace('?', '.')

    # Use regular expression matching
    return re.fullmatch(p, s) is not None

# Example usage
s = "cb2"
# p = "?a"ach
# p = "?b"
p = "c*"
# p = "c?"
# p = "?b "
# p = "?b"

# p = "c*a"
# p = "*bsa"
print(isMatch(s, p))  # Output: False
