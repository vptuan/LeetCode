class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f, n = cost, len(cost)
        for i in range(2, n):
            f[i] = min(f[i-1]+cost[i], f[i-2]+cost[i])
        return min(f[n-1], f[n-2])
