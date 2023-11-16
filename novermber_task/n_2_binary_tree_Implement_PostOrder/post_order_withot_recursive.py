"""
Should use binary tree to Implement PostOrder Traversal Without Recursion.Here use the iterative method to traverse binary tree elements.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorderTraversal(root):
    if not root:
        return []

    stack1 = []
    stack2 = []
    result = []

    stack1.append(root)

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        result.append(node.val)

    return result


# Create a binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

# 4,5,2,3,1
"""
[10,2,1,4,5]
     10
    2   1
  4   5
  
4,5,2,1,10   
"""

root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

postorder_result = postorderTraversal(root)

print("Postorder Traversal Result:")
for element in postorder_result:
    print(element)
