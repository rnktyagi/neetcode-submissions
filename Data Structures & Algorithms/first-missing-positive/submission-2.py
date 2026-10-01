class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start=0

        hashset=set()

        for i in nums :
            hashset.add(i)
        
        missing=True

        while missing :
            if start+1 not in hashset and start+1>0 :
                missing=False
                return start+1
            else :
                start+=1