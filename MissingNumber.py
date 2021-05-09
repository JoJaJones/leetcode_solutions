class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        length = len(nums)
        return (length*(length+1)//2) - total
