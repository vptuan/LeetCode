class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x+1 # to avoid corner case x = 1
        while (l+1 < r):
            c = (l + r + 1) // 2
            # print(l, r, c, c*c) """
            if (c*c <= x):
                l = c
            else:
                r = c
        return l 
