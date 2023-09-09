class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=prices[0]
        max1=0
        for i in prices[1:]:
            max1=max(max1,i-min1)
            min1=min(min1,i)
        return max1
