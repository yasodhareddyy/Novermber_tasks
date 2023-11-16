"""
 You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.
Input: matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
Output: [[7,4,1],
        [8,5,2],
        [9,6,3]]
"""

def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()


# Example usage:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
rotate(matrix)
print(matrix)





