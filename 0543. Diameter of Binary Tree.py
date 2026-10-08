# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
maxDiameter = 0
class Solution(object):
    def maxDepth(self, root):
        """
        return the maxDepth of all nodes to root
        """
        if (root is None):
            return 0 
        global maxDiameter
        maxL, maxR = self.maxDepth(root.left), self.maxDepth(root.right)
        maxDiameter = max(maxL + maxR, maxDiameter)
        return max(maxL, maxR) + 1
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        global maxDiameter
        maxDiameter = 0
        maxL, maxR = self.maxDepth(root.left), self.maxDepth(root.right)
        maxDiameter = max(maxL + maxR, maxDiameter)
        return maxDiameter
