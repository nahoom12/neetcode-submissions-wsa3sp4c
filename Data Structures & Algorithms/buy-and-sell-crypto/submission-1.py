class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        r = 1
        max_profit = 0
        if len(prices) == 1:
            return max_profit
        while r <= len(prices) -1:
            if prices[r] < min_price:
                min_price = prices[r]
                r += 1
            else:
                max_profit = max(max_profit,(prices[r] - min_price))
                r += 1
        return max_profit
        

        


        