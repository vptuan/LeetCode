class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        return 2*sum(set(nums))-sum(nums)
        """
        out = 0
        for n in nums:
            out = out ^ n 
        return out 
