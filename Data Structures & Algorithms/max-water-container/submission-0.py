class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1

        maxWater=float("-inf")

        while L<R :
            ht=min(heights[L] , heights[R])
            wd=R-L

            maxWater=max(maxWater,ht*wd)

            if heights[L]<=heights[R] :
                L+=1
            elif heights[L]>heights[R] :
                R-=1
        
        return maxWater
        