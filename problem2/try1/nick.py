# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):                        
    def maxDepth(self, root):
        return 0 if not root else 1 + max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
