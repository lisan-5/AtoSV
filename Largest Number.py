class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=lambda x: x * 10, reverse=True)
        return ''.join(nums) if nums[0] != '0' else '0'
