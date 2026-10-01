class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=l2=0

        ans=""

        while l1<len(word1) and l2<len(word2) :
            toadd=word1[l1] + word2[l2]
            ans+=toadd
            l1+=1
            l2+=1

        while l1<len(word1) :
            ans+=word1[l1]
            l1+=1
        
        while l2<len(word2) :
            ans+=word2[l2]
            l2+=1
        
        return ans