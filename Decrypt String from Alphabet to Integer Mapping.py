class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                result = chr(int(s[i - 2:i]) + 96) + result
                i -= 3
            else:
                result = chr(int(s[i]) + 96) + result
                i -= 1
        return result
