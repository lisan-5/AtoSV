class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        dq = deque()
        min_length = float('inf')
        
        for i in range(n + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1
