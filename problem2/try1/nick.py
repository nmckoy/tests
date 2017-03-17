# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
      def __init__(self):
                self.depth = 0
                        
                            def maxDepth(self, root):
                                      if not root:
                                                    return 0
                                                          if not root.left and not root.right:
                                                                        return 1
                                                                              left = root.left
                                                                                      right = root.right
                                                                                        return max(self.maxDepth(left) + 1, self.maxDepth(right) + 1)


                                                                                                    
                                                                                                    
