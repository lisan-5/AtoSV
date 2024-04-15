class Solution:
    def similarPairs(self, word: List[str]) -> int:
        c =0
        for n in range(len(word)):
            for m in range(n+1, len(word)):
                if set(word[n]) == set(word[m]):
                   c+=1
        return c
