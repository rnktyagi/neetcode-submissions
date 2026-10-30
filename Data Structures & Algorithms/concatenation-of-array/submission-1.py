class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n=len(nums)
        t=2*n

        arr=[0]*t

        for i in range(0,t) :
            arr[i]=nums[i%n]     

        return arr   