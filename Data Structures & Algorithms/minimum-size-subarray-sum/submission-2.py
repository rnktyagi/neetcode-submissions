class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total=0
        length=float("inf")
        L=0
        R=0
        while R < len(nums) :
            total+=nums[R]

            while total>=target :
                length=min(length, R-L+1)
                total-=nums[L]
                L+=1

            R+=1
        
        return length if length!=float('inf') else 0        