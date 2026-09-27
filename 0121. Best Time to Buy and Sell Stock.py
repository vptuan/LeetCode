class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy = 0
        best = prices[1] - prices[0]
        n = len(prices)
        while buy < n-1:
            while buy < n-1 and prices[buy] >= prices[buy+1]:
                buy += 1
            max_index = buy
            for curr in range(buy+1, n):
                if prices[curr] >= prices[max_index]:
                    max_index = curr
            min_index = buy
            for curr in range(buy+1, max_index):
                if prices[curr] < prices[min_index]:
                    min_index = curr
            if (prices[max_index]-prices[min_index]> best):
                best = prices[max_index]-prices[min_index]
            buy = max_index + 1
        return best if best > 0 else 0
