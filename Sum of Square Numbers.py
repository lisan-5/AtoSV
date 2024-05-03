class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)
        
        while left <= right:
            current_sum = left ** 2 + right ** 2
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        
        return False
