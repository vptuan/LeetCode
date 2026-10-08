# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0

        def maxDepth(root):
            """
            return the maxDepth of all nodes to root
            """
            if (root is None):
                return 0 
            maxL, maxR = maxDepth(root.left), maxDepth(root.right)
            self.max_diameter = max(maxL + maxR, self.max_diameter)
            return max(maxL, maxR) + 1

        if root is None:
            return 0

        maxDepth(root)
        return self.max_diameter
