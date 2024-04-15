class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = []
    
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                max_value = grid[i][j]
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        max_value = max(max_value, grid[i + dx][j + dy])
                row.append(max_value)
            max_local.append(row)
    
        return max_local
