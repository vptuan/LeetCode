# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return (lambda s: s(s, root.left, root.right))(lambda self, p, q: (p.val == q.val) and self(self, p.left, q.right) and self(self, p.right, q.left) if (p and q) else p == q)
