"""
Plot the reference counts graph for 26 English letters.
Example output should be below:
"""

import matplotlib.pyplot as plt
# Define the counts for each letter (you can adjust these values as needed)
letter_counts = {
    'a': 1200, 'b': 1000, 'c': 800, 'd': 600, 'e': 400, 'f': 200,
    'g': 100, 'h': 800, 'i': 500, 'j': 300, 'k': 200, 'l': 100,
    'm': 800, 'n': 600, 'o': 500, 'p': 300, 'q': 200, 'r': 100,
    's': 1000, 't': 800, 'u': 600, 'v': 400, 'w': 200, 'x': 100,
    'y': 500, 'z': 300,
}

# Extract letters and their corresponding counts
letters = list(letter_counts.keys())
counts = list(letter_counts.values())

# Create the reference counts graph
plt.figure(figsize=(10, 4))
plt.bar(letters, counts)
# plt.scatter(letters, counts)
# plt.plot(letters, counts)
plt.xlabel('Letters')
plt.ylabel('Reference Counts')
plt.title('Reference Counts for English Letters')
plt.show()


