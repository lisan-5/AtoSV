class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['.'] * n for _ in range(m)]
        
        for guard in guards:
            grid[guard[0]][guard[1]] = 'G'
        for wall in walls:
            grid[wall[0]][wall[1]] = 'W'
        
        def mark_guarded(r, c, dr, dc):
            while 0 <= r < m and 0 <= c < n:
                if grid[r][c] in 'GW':
                    break
                if grid[r][c] == '.':
                    grid[r][c] = 'X'
                r += dr
                c += dc
        
        for guard in guards:
            r, c = guard
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                mark_guarded(r + dr, c + dc, dr, dc)
        
        return sum(row.count('.') for row in grid)
