class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars=sorted(zip(position, speed))

        times=[]

        for p,s in cars :
            times.append((target-p)/s)
        
        res=[]
        
        for t in reversed(times) :
            if not res :
                res.append(t)
            
            elif t<=res[-1] :
                continue
            
            else :
                res.append(t)
        
        return len(res)
        