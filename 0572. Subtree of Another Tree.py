# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, r, subR):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSameTree(p, q):
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right) if p and q else (p == q) 
        
        return isSameTree(r, subR) or self.isSubtree(r.left, subR) or self.isSubtree(r.right, subR) if r else r == subR
        
