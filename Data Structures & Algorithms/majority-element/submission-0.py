class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit= int(len(nums)/2)

        hashmap={}

        for i in nums :
            hashmap[i]=hashmap.get(i, 0)+1
        
        for k,v in hashmap.items() :
            if v>limit :
                return k
        