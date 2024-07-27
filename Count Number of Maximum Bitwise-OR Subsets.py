class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            return backtrack(index + 1, current_or) + backtrack(index + 1, current_or | nums[index])
        
        max_or = 0
        for num in nums:
            max_or |= num
        
        return backtrack(0, 0)
