class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        Ans = Fibonacci series
        """
        f1 = 0
        f2 = 1
        for i in range(n):
            f1, f2 = f2, f1 + f2
        return f2
