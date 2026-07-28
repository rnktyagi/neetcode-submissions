class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(0,len(nums)) :
            L=i+1
            R=len(nums)-1

            while L<R :
                if(nums[i]+nums[L] + nums[R] < 0) :
                    L+=1
                elif(nums[i]+nums[L] + nums[R] > 0) :
                    R-=1
                else :
                    if [nums[i],nums[L],nums[R]] not in ans :
                        ans.append([nums[i],nums[L],nums[R]])
                    L+=1
                    R-=1

        return ans

                
        