class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_n = n * (n + 1) // 2
        sum_nums = sum(set(nums))
        sum_actual = sum(nums)
        
        duplicate = sum_actual - sum_nums
        missing = sum_n - sum_nums
        
        return [duplicate, missing]
