class Solution:
    def minSwaps(self, arr: List[int]) -> int:
        def solve(l, r):
            if r - l == 1:
                return 0

            mid = (l + r) // 2
            left_sorted = sorted(arr[l:mid])
            right_sorted = sorted(arr[mid:r])

            if left_sorted[-1] <= right_sorted[0]:
                return solve(l, mid) + solve(mid, r)

            if right_sorted[-1] <= left_sorted[0]:
                return solve(l, mid) + solve(mid, r)

            arr[l:mid], arr[mid:r] = arr[mid:r], arr[l:mid]
            return solve(l, mid) + solve(mid, r) + 1

        n = len(arr)
        result = solve(0, n)
        left_sorted = sorted(arr[:n//2])
        right_sorted = sorted(arr[n//2:])

        if left_sorted[-1] <= right_sorted[0]:
            return result
        return -1
