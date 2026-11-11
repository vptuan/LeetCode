class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0 
        for i in range(32):
            if n & (1 << i):
                m = m | (1 << (31-i))
        return m
