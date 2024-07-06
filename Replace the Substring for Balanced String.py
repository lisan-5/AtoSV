class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = {char: s.count(char) for char in 'QWER'}
        min_length = n
        left = 0

        for right in range(n):
            count[s[right]] -= 1
            while left < n and all(count[char] <= n // 4 for char in 'QWER'):
                min_length = min(min_length, right - left + 1)
                count[s[left]] += 1
                left += 1

        return min_length
