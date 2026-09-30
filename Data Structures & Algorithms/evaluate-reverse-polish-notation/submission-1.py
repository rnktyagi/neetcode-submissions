class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for i in tokens :
            if i=="+" :
                second=stack.pop()
                first=stack.pop()
                stack.append(first+second)

            elif i=="-" :
                second=stack.pop()
                first=stack.pop()
                stack.append(first-second)
            
            elif i=="*" :
                second=stack.pop()
                first=stack.pop()
                stack.append(first*second)

            elif i=="/" :
                second=stack.pop()
                first=stack.pop()
                stack.append(int(first/second))
            
            else :
                stack.append(int(i))
    
        return stack.pop()



