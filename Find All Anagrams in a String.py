class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        r = []
        target_counts = collections.Counter(p)
        window_counts = collections.Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            curr_char = s[i]
            window_counts[curr_char] += 1
            if window_counts == target_counts:
                r.append(i - len(p) + 1)
            window_counts[s[i - len(p) + 1]] -= 1
            if window_counts[s[i - len(p) + 1]] == 0:
                del window_counts[s[i - len(p) + 1]]
        return r
