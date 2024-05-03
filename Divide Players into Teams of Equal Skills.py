class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_sum = sum(skill)
        if total_sum % (len(skill) // 2) != 0:
            return -1
        
        target_sum = total_sum // (len(skill) // 2)
        skill.sort()
        
        chemistry_sum = 0
        left, right = 0, len(skill) - 1
        
        while left < right:
            if skill[left] + skill[right] != target_sum:
                return -1
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry_sum
