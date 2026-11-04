class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones)>1:
            x, y = stones[-2], stones[-1]
            stones = stones[:-2]
            if (x != y):
                bisect.insort(stones, y-x)
        return stones[0] if stones else 0
        
