# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.helper(root)
        
        
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        return max(left, right) + 1

