class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy, sell = 0,1
        
        for i, v in enumerate(prices):
            if sell > len(prices)-1: break
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                maxProfit = max(maxProfit, prices[sell]-prices[buy])
            sell += 1
        
            
        return maxProfit
        