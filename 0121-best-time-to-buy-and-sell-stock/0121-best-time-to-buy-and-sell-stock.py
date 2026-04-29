class Solution(object):
    def maxProfit(self, prices):
        min_value=float('inf')
        max_profit=0

        for price in prices:
            if price < min_value:
                min_value=price
            else:
                profit=price-min_value
                max_profit=max(profit,max_profit)
        
        return max_profit
        