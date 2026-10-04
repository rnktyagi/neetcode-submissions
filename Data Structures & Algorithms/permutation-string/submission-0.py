class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)

        L=0

        freq=[0]*26

        s1_freq=[0]*26

        for i in s1 :
            index=ord(i)-ord('a')

            s1_freq[index]+=1
        
        for R in range(len(s2)) :
            if R-L+1 < k :
                index=ord(s2[R])-ord('a')
                freq[index]+=1
            
            else :
                index=ord(s2[R])-ord('a')
                freq[index]+=1
                if freq==s1_freq :
                    return True
                
                Lindex=ord(s2[L])-ord('a')
                freq[Lindex]-=1
                L+=1
        
        return False