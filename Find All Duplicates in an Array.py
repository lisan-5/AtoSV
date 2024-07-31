class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                res.append(index + 1)
            nums[index] = -nums[index]
        return res
