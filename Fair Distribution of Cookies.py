class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(i, distributions):
            if i == len(cookies):
                return max(distributions)
            min_unfairness = float('inf')
            for j in range(k):
                distributions[j] += cookies[i]
                min_unfairness = min(min_unfairness, backtrack(i + 1, distributions))
                distributions[j] -= cookies[i]
                if distributions[j] == 0:
                    break
            return min_unfairness
        
        return backtrack(0, [0] * k)
