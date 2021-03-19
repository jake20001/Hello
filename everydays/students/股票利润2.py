class Solution:
    def maxProfit2(self, prices) -> int:
        p = 0
        a = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                a += (prices[i - 1] - prices[p])
                p = i
        s = prices[-1] - prices[p]
        if s > 0:
            a += s
        return a

    def maxProfit(self, prices) -> int:
        p = 0
        a = 0
        for i in range(1, len(prices)):
            if prices[i]-prices[i - 1]>0:
                a += (prices[i]-prices[i - 1])
                p = i
        s = prices[-1] - prices[p]
        if s > 0:
            a += s
        return a

a=Solution()
print(a.maxProfit([7,1,5,3,6,4]))