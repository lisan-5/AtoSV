class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = [set() for _ in range(n)]

        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            connected[u].add(v)
            connected[v].add(u)

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j] - (1 if j in connected[i] else 0)
                max_rank = max(max_rank, rank)

        return max_rank
