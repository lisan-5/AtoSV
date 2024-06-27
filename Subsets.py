class Solution:
    def subsets(self, nums):
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        res = []
        backtrack(0, [])
        return res
