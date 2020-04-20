# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def insert(node, val):
    if node == None:
        node = TreeNode(val)
    elif val <= node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        for val in preorder:
            root = insert(root, val)
        return root
