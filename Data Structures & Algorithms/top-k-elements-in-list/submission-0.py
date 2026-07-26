class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap={}

        for n in nums :
            hashMap[n] = 1 + hashMap.get(n , 0)

        sortList=[]

        for key,value in hashMap.items() :
            sortList.append([value,key])

        sortList.sort(reverse=True)

        ans=[]

        for i in range(0,k) :
            ans.append(sortList[i][1])
        
        return ans