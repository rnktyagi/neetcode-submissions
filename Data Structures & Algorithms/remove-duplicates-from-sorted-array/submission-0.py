class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l1=0
        l2=1

        while l2<len(nums) :
            if nums[l1]==nums[l2] :
                nums.pop(l2)
            
            else :
                l1+=1
                l2+=1

        return len(nums)