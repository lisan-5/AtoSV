class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        mod_dict = {0: 1}
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            
            if mod < 0:
                mod += k
                
            if mod in mod_dict:
                count += mod_dict[mod]
                mod_dict[mod] += 1
            else:
                mod_dict[mod] = 1
                
        return count
