class Solution:
    def circularArrayLoop(self, nums):
        def next_index(i):
            return (i + nums[i]) % len(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            
            slow, fast = i, next_index(i)
            while nums[fast] * nums[i] > 0 and nums[next_index(fast)] * nums[i] > 0:
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
                
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            
            slow, val = i, nums[i]
            while nums[slow] * val > 0:
                next_slow = next_index(slow)
                nums[slow] = 0
                slow = next_slow
        
        return False
