class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le = 0
        
        if len(s) ==0:
            return 0
        if len(s) == 1:
            return 1

        ptr1 = 0
        ptr2 = 1

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in s[i:j]:
                    break
                else:
                    le = max(le, j-i+1)

        return le
