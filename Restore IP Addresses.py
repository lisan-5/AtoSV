class Solution:
    def restoreIpAddresses(self, s):
        def backtrack(start=0, parts=[]):
            if len(parts) == 4 and start == len(s):
                result.append(".".join(parts))
                return
            if len(parts) == 4 or start == len(s):
                return
            
            for i in range(1, 4):
                if start + i > len(s):
                    break
                segment = s[start:start + i]
                if (segment[0] == "0" and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(start + i, parts + [segment])
        
        result = []
        backtrack()
        return result
