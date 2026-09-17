# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        this function from the MaxDepthTree in Q104
        """
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0 
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return (not root) or (self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.maxDepth(root.left)-self.maxDepth(root.right)) <= 1) 
