class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in s :
            if i==']' :
                substring=""
                while stack and stack[-1]!='[' :
                    substring=stack.pop()+substring
                
                stack.pop()
                
                digit=""

                while stack and stack[-1].isnumeric() :
                    digit=stack.pop()+digit
                
                digit=int(digit)
                stack.append(digit*substring)
            
            else :
                stack.append(i)
        
        return "".join(stack)
        