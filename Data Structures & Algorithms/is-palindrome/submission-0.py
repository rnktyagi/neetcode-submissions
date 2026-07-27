class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[i.lower() for i in s if i.isalnum()]
        L=0
        R=len(s)-1

        while L < R :
            if s[L] != s[R] :
                return False
            else :
                L+=1
                R-=1

        return True
            
            

        