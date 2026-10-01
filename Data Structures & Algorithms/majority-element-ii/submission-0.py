class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        limit=int(len(nums)/3)

        hashmap={}

        for i in nums :
            hashmap[i]=hashmap.get(i,0)+1
        
        ans=[]

        for k,v in hashmap.items() :
            if v>limit :
                ans.append(k)
        
        return ans
        