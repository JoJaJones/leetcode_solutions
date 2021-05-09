class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [1,1]
        for i in range(2, n + 1):
            memo.append(memo[-1] + memo[-2])
        
        return memo[-1]
