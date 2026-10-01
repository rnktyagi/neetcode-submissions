class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for i in operations :
            if i=="+" :
                f=stack[-1]
                s=stack[-2]

                stack.append(f+s)
            
            elif i=='D' :
                f=stack[-1]
                stack.append(f*2)
            
            elif i=='C' :
                stack.pop()
            
            else :
                stack.append(int(i))
        
        return sum(stack)