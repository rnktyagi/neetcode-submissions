class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 :
            return 0
        nums.sort()

        maxLength=0
        length=0

        for i in range(1,len(nums)) :
            if nums[i]-nums[i-1]==1 :
                length+=1
            elif nums[i]==nums[i-1] :
                continue
            else :
                maxLength=max(maxLength,length)
                length=0
            maxLength=max(length,maxLength)

        return maxLength+1

