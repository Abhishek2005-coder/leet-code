class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Track the minimum buying price seen so far
            if price < min_price:
                min_price = price
            # Calculate current profit if sold today and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit