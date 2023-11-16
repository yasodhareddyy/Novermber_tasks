import numpy as np

def rotate(matrix):
    rotated_matrix = np.rot90(matrix, k=-1)
    np.copyto(matrix, rotated_matrix)

# Example usage:
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

rotate(matrix)
print(matrix)
