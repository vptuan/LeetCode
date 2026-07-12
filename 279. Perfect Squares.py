class Solution:
    def numSquares(self, n: int) -> int:
        if int(n**0.5)**2 == n:
            return 1
        for a in range(1, int((n//2)**0.5)+1):
            bb = n-a*a
            if int(bb**0.5)**2 == bb:
                return 2
        #check if n in the format of 4^k(8m+7) => 4, else 3 based on Lagrange's four-square theorem
        while n%4 == 0:
            n = n //4
        if (n % 8 == 7):
            return 4
        else:
            return 3
