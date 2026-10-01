class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                s1 = s[:l] + s[l+1:]
                s2 = s[:r] + s[r+1:]

                if s1 == s1[::-1]:
                    return True

                if s2 == s2[::-1]:
                    return True

                return False

            l += 1
            r -= 1

        return True