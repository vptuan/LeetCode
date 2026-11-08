class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        1)
        return sum(map(int, bin(n)[2:]))
        2) 
        sum = 0
        while n>0:
            sum += n & 1
            n = n >> 1
        return sum        
        3) 
        sum = 0
        while n>0:
            n = n & (n-1)
            sum += 1
        return sum        
        """
        return 0 if n==0 else 1+ self.hammingWeight(n & (n-1))
