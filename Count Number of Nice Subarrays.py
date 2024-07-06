class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_counts = {0: 1}
        current_odd_count = 0
        
        for num in nums:
            if num % 2 == 1:
                current_odd_count += 1
            if current_odd_count - k in prefix_counts:
                count += prefix_counts[current_odd_count - k]
            if current_odd_count in prefix_counts:
                prefix_counts[current_odd_count] += 1
            else:
                prefix_counts[current_odd_count] = 1
        
        return count
