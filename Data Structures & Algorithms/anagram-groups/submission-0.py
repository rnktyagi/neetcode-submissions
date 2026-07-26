class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for s in strs :
            freqList = [0]*26

            for i in s :
                freqList[ord(i) - ord('a')]+=1

            freqTuple = tuple(freqList)

            if freqTuple in hashMap :
                hashMap[freqTuple].append(s)
            else :
                hashMap[freqTuple] = [s]

        return list(hashMap.values())

        
        
