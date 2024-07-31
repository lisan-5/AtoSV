class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
