def isMatch(s, p):
    if not p:
        return not s

    first_match = bool(s) and (s[0] == p[0] or p[0] == '?')

    if p[0] == '*':
        return isMatch(s, p[1:]) or (bool(s) and isMatch(s[1:], p))
    else:
        return first_match and isMatch(s[1:], p[1:])

# Example usage
s = "cbhj  "
p = "?a"
# p = "c?hj "
print(isMatch(s, p))  # Output: False
