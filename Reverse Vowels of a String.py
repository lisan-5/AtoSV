class Solution:
    def reverseVowels(self, s: str) -> str:
        a = []
        
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                a.append(s[i])
        a = a[::-1]
        val = 0
        
        ans = ""
        
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                ans+= a[val]
                val+=1
            else:
                ans+= s[i]
        
        return ans
