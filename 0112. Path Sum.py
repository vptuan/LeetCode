# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if (not root): # root == NULL, return False as requested (no root-to-leaf paths.)
            return False
        # if not root.left and not root.right: # no left and no right -> leaf node 
        return (targetSum == root.val) if not root.left and not root.right else self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
