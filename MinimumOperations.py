# this is a modified longest common subsequence DP problem.
#
# there is additional room for optimization in this solution since the target 
# sequence is guaranteed to be repeat free otherwise this would be optimal

class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        # minor optimization to remove items from arr not in target
        t_items = {item: index for index, item in enumerate(target)}
        new_arr = []
        for val in arr:
            if val in t_items:
                new_arr.append(val)
        
        memo = [[0 for _ in range(len(new_arr)+1)] for _ in range(len(target)+1)]
        for i, val in enumerate(target):
            for j, num in enumerate(new_arr):
                memo[i+1][j+1] = self.calc_value(memo, i+1, j+1, val == num)
        
        return len(target) - memo[-1][-1]
        
        
    def calc_value(self, memo, r, c, is_match=False):
        vals = [memo[r][c-1], memo[r - 1][c]]
        if is_match:
            vals.append(memo[r-1][c-1] + 1)

        return max(vals)
