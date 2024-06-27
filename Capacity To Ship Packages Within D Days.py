class Solution:
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            days = 1
            current_weight = 0
            
            for weight in weights:
                if current_weight + weight > mid:
                    days += 1
                    current_weight = 0
                current_weight += weight
            
            if days > D:
                left = mid + 1
            else:
                right = mid
        
        return left
