class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)-1

        while low<=high :
            mid=(low+high)//2

            if matrix[mid][0]>target :
                high=mid-1
            
            elif matrix[mid][-1]<target :
                low=mid+1
            
            else :
                break
        
        if low>high :
            return False
        
        row=(high+low)//2

        l,r=0,len(matrix[row])

        while l<=r :
            m=(l+r)//2

            if target > matrix[row][m] :
                l=m+1

            elif target < matrix[row][m] :
                r=m-1
            
            else : 
                return True
            
        return False
        
        