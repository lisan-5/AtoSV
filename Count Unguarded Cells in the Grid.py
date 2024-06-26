class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['.'] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 'G'
        for r, c in walls:
            grid[r][c] = 'W'
        
        for r, c in guards:
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '.':
                    grid[nr][nc] = 'X'
                    nr, nc = nr + dr, nc + dc

        return sum(cell == '.' for row in grid for cell in row)
