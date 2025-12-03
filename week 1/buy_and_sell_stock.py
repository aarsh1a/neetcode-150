# set min and maxprofit move left to right calculate profit along the way and update if higher than max profit, update min if price lower than min
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            price=prices[i]
            profit=price-min
            if profit>maxProfit:
                maxProfit=profit
            if price<min:
                min=price
        return maxProfit