class Solution:
    def maxIceCream(self, costs, coins):
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        
        for cost in costs:
            count[cost] += 1
        
        total_bars = 0
        
        for cost in range(1, max_cost + 1):
            if coins < cost:
                break
            if count[cost] > 0:
                bars_to_buy = min(count[cost], coins // cost)
                total_bars += bars_to_buy
                coins -= bars_to_buy * cost
        return total_bars
