class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < low:
                low = price
            elif price - low > max_profit:
                max_profit = price - low
        
        return max_profit
