class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = []

        for interval in intervals:
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                if starts[mid][0] >= interval[1]:
                    right = mid
                else:
                    left = mid + 1
            res.append(starts[left][1] if starts[left][0] >= interval[1] else -1)

        return res
