class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolors = float('inf')
        current_recolors = 0

        for i in range(len(blocks)):
            if blocks[i] == 'W':
                current_recolors += 1
            if i >= k and blocks[i - k] == 'W':
                current_recolors -= 1
            if i >= k - 1:
                min_recolors = min(min_recolors, current_recolors)

        return min_recolors
