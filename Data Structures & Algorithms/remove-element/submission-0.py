class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        occ=nums.count(val)

        for i in range(occ) :
            nums.remove(val)
        
        return len(nums)
        