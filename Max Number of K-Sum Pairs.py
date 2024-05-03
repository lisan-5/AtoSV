class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        operations = 0
        
        for num in nums:
            complement = k - num
            if complement in freq and freq[complement] > 0:
                operations += 1
                freq[complement] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1
        
        return operations
