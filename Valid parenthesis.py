class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []

        c = {"(": ")" , "{":"}", "[": "]"}
        for i in s:
            if(i =="[" or i=="{" or i=="("):
                stack.append(i)
            else:
                if(len(stack) ==0 ):
                    return False

                if(c[stack.pop()] != i ):
                    return False
                
        if(len(stack) == 0):
            return True
        else:
            return False
            
        
