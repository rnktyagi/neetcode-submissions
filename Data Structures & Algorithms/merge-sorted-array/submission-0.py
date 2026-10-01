class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l1=l2=0

        ans=[]

        while l1<m and l2<n :
            if nums1[l1]<=nums2[l2] :
                ans.append(nums1[l1])
                l1+=1
            else :
                ans.append(nums2[l2])
                l2+=1
        
        while l1<m :
            ans.append(nums1[l1])
            l1+=1
        
        while l2<n :
            ans.append(nums2[l2])
            l2+=1
        
        nums1[:] = ans
        