class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start, prev_val):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                curr_val = int(s[start:end])
                if prev_val is None or curr_val == prev_val - 1:
                    if backtrack(end, curr_val):
                        return True
            return False
        
        for i in range(1, len(s)):
            if backtrack(i, int(s[:i])):
                return True
        return False
