class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_num,min_num = 0,prices[0]
        for i in range(len(prices)):
            if prices[i] > min_num:
                max_num = prices[i]
                profit = max(profit,max_num - min_num)
            if prices[i] < min_num:
                min_num = prices[i]
        return profit



        