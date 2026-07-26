class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]

        total=1

        for i in nums :
            total=total*i
            prefix.append(total)

        total=1

        for i in reversed(nums) :
            total=total*i
            postfix.append(total)

        postfix.reverse()

        ans=[]
        length=len(nums)

        for i in range(0,length) :
            if i==0 :
                ans.append(postfix[i+1])
            elif i==length-1 :
                ans.append(prefix[i-1])
            else :
                ans.append(postfix[i+1]*prefix[i-1])

        return ans

        