class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=0

        profit=0

        R=1

        while R<len(prices) :
            if prices[L] < prices[R] :
                curr=prices[R]-prices[L]
                profit=max(profit, curr)
            else :
                L=R
            
            R+=1
        
        return profit