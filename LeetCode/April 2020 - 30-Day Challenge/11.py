# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def h(node):
    return 0 if node == None else 1 + max(h(node.left), h(node.right))
    
def d(node):
    return 0 if node == None else max(h(node.left) + h(node.right), d(node.left), d(node.right))

class Solution:
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return d(root)
