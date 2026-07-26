class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}

        for i in range(0,len(nums)) :
            hashMap[nums[i]] = i

        for i in range(0,len(nums)) :
            diff = target-nums[i]
            if diff in hashMap and hashMap[diff]!=i:
                return [i , hashMap[diff]]
                
        