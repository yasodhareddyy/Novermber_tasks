"""

 Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column.
There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
Return the vertical order traversal of the binary tree.
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root):
    if not root:
        return []

    # Create a dictionary to store nodes by their column positions
    column_nodes = {}

    # Use a list for the BFS traversal
    queue = [(root, 0, 0)]

    while queue:
        node, row, col = queue.pop(0)

        # Store the node in the dictionary by its column position
        if col in column_nodes:
            column_nodes[col].append(node.val)
        else:
            column_nodes[col] = [node.val]

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    # Sort the nodes within each column by their values
    sorted_columns = sorted(column_nodes.items(), key=lambda x: x[0])
    result = [[val for val in nodes] for i, nodes in sorted_columns]

    return result

# Example input tree: [3, 9, 20, None, None, 15, 7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the vertical order traversal
result = verticalOrder(root)
print(result)
