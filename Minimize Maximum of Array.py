class Solution:
    def minimizeArrayValue(self, nums):
        prefix_sum = 0
        max_value = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            max_value = max(max_value, (prefix_sum + i) // (i + 1))
        return max_value
