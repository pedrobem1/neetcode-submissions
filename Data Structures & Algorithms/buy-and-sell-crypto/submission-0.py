class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in prices[1:]:
            profit = i - min_price
            if profit > max_profit:
                max_profit = profit
            if i < min_price:
                min_price = i
        return max_profit