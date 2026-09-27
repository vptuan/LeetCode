class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        min_index = 0
        best = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] < prices[min_index]:
                min_index = i
            if prices[i]-prices[min_index]> best:
                best = prices[i]-prices[min_index]
                           
        return best if best > 0 else 0
