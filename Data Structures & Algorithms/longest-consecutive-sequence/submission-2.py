class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap=set()

        for n in nums :
            hashMap.add(n)

        starters=[]
        for i in hashMap :
            if i-1 not in hashMap :
                starters.append(i)

        maxLength=0
        for k in starters :
            length=1

            while k+1 in hashMap :
                length+=1
                k+=1

            maxLength=max(maxLength,length)

        return maxLength



